import chromadb
import os
from chromadb.utils import embedding_functions
from core.visa_data import VISA_DATA, normalize_country

embedding_function = embedding_functions.DefaultEmbeddingFunction()
client = chromadb.PersistentClient(path="./chroma_visa_db")

def get_collection():
    return client.get_or_create_collection(
        name="visa_requirements",
        embedding_function=embedding_function,
        metadata={"hnsw:space": "cosine"}
    )

def build_knowledge_base():
    collection = get_collection()
    if collection.count() >= len(VISA_DATA):
        print("Visa knowledge base already built. Skipping.")
        return
    print("Building visa knowledge base...")
    documents = []
    ids = []
    metadatas = []
    for entry in VISA_DATA:
        doc_text = f"""Country: {entry['country']}
Visa Type: {entry['visa_type']}
Visa Required: {'Yes' if entry['visa_required'] else 'No'}
Processing Time: {entry['processing_time']}
Fee: {entry['fee']}
Validity: {entry['validity']}
Interview Required: {'Yes' if entry['interview_required'] else 'No'}
Required Documents: {', '.join(entry['required_documents'])}
Important Notes: {entry['notes']}""".strip()
        documents.append(doc_text)
        ids.append(entry['code'])
        metadatas.append({"country": entry['country'], "code": entry['code'], "fee": entry['fee']})
    collection.add(documents=documents, ids=ids, metadatas=metadatas)
    print(f"Knowledge base built with {len(VISA_DATA)} countries.")

def query_visa_requirements(user_query: str, n_results: int = 2):
    normalized_query = normalize_country(user_query)
    collection = get_collection()
    results = collection.query(query_texts=[normalized_query], n_results=n_results)
    if not results["documents"][0]:
        return None, normalized_query
    return results["documents"][0], normalized_query

build_knowledge_base()
