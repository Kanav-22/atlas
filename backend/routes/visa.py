import os
import shutil
import uuid
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from core.visa_service import query_visa_requirements
from core.document_analyzer import extract_text_from_pdf, analyze_documents
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@router.get("/visa/requirements")
def get_visa_requirements(country: str):
    """
    Get visa requirements for a country using RAG.
    Automatically handles Schengen countries.
    """
    retrieved_chunks, normalized_query = query_visa_requirements(country)

    if not retrieved_chunks:
        return {"error": f"No visa information found for {country}"}

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""You are a visa expert helping Indian passport holders.
Based on the following visa information, answer this query: "{country}"

RETRIEVED VISA INFORMATION:
{context}

Provide a clear, structured response with:
1. Visa type and whether it's required
2. Key documents needed (as a list)
3. Processing time and fee
4. Important tips or warnings

End with: "⚠️ Always verify requirements at the official embassy website before applying."
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=800
    )

    return {
        "country": country,
        "normalized_query": normalized_query,
        "answer": response.choices[0].message.content,
        "source_chunks": retrieved_chunks
    }


@router.post("/visa/analyze")
async def analyze_visa_documents(
    country: str = Form(...),
    files: list[UploadFile] = File(...)
):
    """
    Upload documents and get gap analysis against visa requirements.
    """
    # Step 1: Get visa requirements via RAG
    retrieved_chunks, _ = query_visa_requirements(country)
    if not retrieved_chunks:
        return JSONResponse(
            status_code=404,
            content={"error": f"No visa information found for {country}"}
        )

    visa_requirements = "\n\n".join(retrieved_chunks)

    # Step 2: Save and extract text from uploaded PDFs
    extracted_texts = {}
    temp_dir = f"/tmp/visa_{uuid.uuid4().hex[:8]}"
    os.makedirs(temp_dir, exist_ok=True)

    try:
        for file in files:
            if not file.filename.endswith(".pdf"):
                extracted_texts[file.filename] = f"[Non-PDF file — cannot extract text]"
                continue

            file_path = os.path.join(temp_dir, file.filename)
            with open(file_path, "wb") as f:
                shutil.copyfileobj(file.file, f)

            text = extract_text_from_pdf(file_path)
            extracted_texts[file.filename] = text

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    # Step 3: Run gap analysis
    analysis = analyze_documents(extracted_texts, visa_requirements, country)

    return {
        "country": country,
        "documents_uploaded": list(extracted_texts.keys()),
        "analysis": analysis
    }