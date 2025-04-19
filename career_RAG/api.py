from fastapi import FastAPI, Request
from pydantic import BaseModel
from rag_pipeline import load_rag_pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
qa = load_rag_pipeline()

# Allow Gradio (or any frontend) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_rag(request: QueryRequest):
    answer = qa.run(request.question)
    return {"response": answer}
