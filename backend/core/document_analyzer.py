import os
import json
from pypdf import PdfReader
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(file_path: str) -> str:
    """Extract all text from a PDF file"""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def analyze_documents(extracted_texts: dict, visa_requirements: str, country: str) -> dict:
    """
    Compare user's uploaded documents against visa requirements.
    extracted_texts: {filename: extracted_text}
    visa_requirements: the retrieved visa checklist from ChromaDB
    country: destination country
    """
    # Build a summary of what documents the user has
    docs_summary = ""
    for filename, text in extracted_texts.items():
        docs_summary += f"\n--- Document: {filename} ---\n{text[:500]}\n"

    prompt = f"""You are a visa document checker for Indian passport holders applying for {country}.

VISA REQUIREMENTS:
{visa_requirements}

USER'S UPLOADED DOCUMENTS:
{docs_summary}

Analyze the uploaded documents against the visa requirements. Return ONLY valid JSON:

{{
  "country": "{country}",
  "fulfilled": [
    {{"document": "document name", "status": "found", "detail": "brief explanation"}}
  ],
  "missing": [
    {{"document": "document name", "status": "missing", "detail": "what is needed"}}
  ],
  "warnings": [
    {{"document": "document name", "status": "warning", "detail": "needs verification"}}
  ],
  "overall_status": "ready" or "incomplete" or "needs_review",
  "summary": "2 sentence summary of readiness"
}}

Be practical — if a bank statement is uploaded, mark bank statements as fulfilled even if you cannot verify the exact balance. Focus on document presence, not content verification."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=1000
    )

    raw = response.choices[0].message.content
    try:
        # Clean any markdown formatting
        clean = raw.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except:
        return {
            "error": "Could not parse analysis",
            "raw": raw,
            "overall_status": "needs_review",
            "summary": "Please review your documents manually."
        }