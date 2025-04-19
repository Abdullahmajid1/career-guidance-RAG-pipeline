from langchain.llms import HuggingFaceHub
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
load_dotenv()


def load_rag_pipeline():
    db = Chroma(persist_directory="career_db", embedding_function=HuggingFaceEmbeddings())
    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        model_kwargs={"temperature": 0.3, "max_new_tokens": 512}
    )

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
    return qa_chain
