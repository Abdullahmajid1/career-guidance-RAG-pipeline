from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def ingest_documents():
    loader = PyPDFLoader("data/0e596882-en.pdf")
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(pages)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(docs, embedding=embeddings, persist_directory="career_db")
    db.persist()
    print("✅ Career document embedded and stored!")

if __name__ == "__main__":
    ingest_documents()
