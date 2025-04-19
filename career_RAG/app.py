import gradio as gr
import requests

API_URL = "http://localhost:8000/query"  

def ask_backend(question):
    response = requests.post(API_URL, json={"question": question})
    return response.json()["response"]

iface = gr.Interface(
    fn=ask_backend,
    inputs=gr.Textbox(label="Ask a career question"),
    outputs="text",
    title="Career Guidance Assistant",
    description="Powered by a Hugging Face RAG pipeline with backend API"
)

iface.launch()

