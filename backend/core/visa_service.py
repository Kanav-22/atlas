import chromadb
import json
import os
from sentence_transformers import SentenceTransformer
from core.visa_data import VISA_DATA, normalize_country

# Load the transformer model (runs locally, no API needed)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Set up ChromaDB with persistent storage
client = chromadb.PersistentClient(path="./chroma_visa_db")

def get_collection():
    return client.get_or_create_collection(
        name="visa_requirements",
        metadata={"hnsw:space": "cosine"}
    )

def build_knowledge_base():
    """
    Convert all visa data into vectors and store in ChromaDB.
    This runs once — subsequent calls skip if already built.
    """
    collection = get_collection()

    # Skip if already populated
    if collection.count() >= len(VISA_DATA):
        print("Visa knowledge base already built. Skipping.")
        return

    print("Building visa knowledge base...")

    documents = []
    embeddings = []
    ids = []
    metadatas = []

    for entry in VISA_DATA:
        # Create a rich text document for each country
        doc_text = f"""
Country: {entry['country']}
Visa Type: {entry['visa_type']}
Visa Required: {'Yes' if entry['visa_required'] else 'No - ' + entry['visa_type']}
Processing Time: {entry['processing_time']}
Fee: {entry['fee']}
Validity: {entry['validity']}
Interview Required: {'Yes' if entry['interview_required'] else 'No'}
Required Documents: {', '.join(entry['required_documents'])}
Important Notes: {entry['notes']}
        """.strip()

        # Convert to vector using transformer model
        embedding = model.encode(doc_text).tolist()

        documents.append(doc_text)
        embeddings.append(embedding)
        ids.append(entry['code'])
        metadatas.append({
            "country": entry['country'],
            "code": entry['code'],
            "visa_required": str(entry['visa_required']),
            "fee": entry['fee'],
            "processing_time": entry['processing_time']
        })

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )

    print(f"Knowledge base built with {len(VISA_DATA)} countries.")

def query_visa_requirements(user_query: str, n_results: int = 2):
    """
    Main RAG query function.
    1. Normalize query (handle Schengen countries)
    2. Convert query to vector
    3. Find most similar chunks in ChromaDB
    4. Return the retrieved documents
    """
    # Step 1: Normalize — redirect Schengen countries
    normalized_query = normalize_country(user_query)

    # Step 2: Convert query to vector
    query_embedding = model.encode(normalized_query).tolist()

    # Step 3: Search ChromaDB
    collection = get_collection()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    if not results["documents"][0]:
        return None, normalized_query

    # Return the retrieved documents and the normalized query
    return results["documents"][0], normalized_query

# Build knowledge base when this module is imported
build_knowledge_base()