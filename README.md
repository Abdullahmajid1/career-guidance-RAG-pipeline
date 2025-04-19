
# 🎓 Career Guidance Assistant (AIDI 2001 Final Project)

An intelligent AI assistant that helps students explore personalized career options using a Retrieval-Augmented Generation (RAG) pipeline powered by Hugging Face models. Built with LangChain, FastAPI, Gradio, and ChromaDB.

---

## 📌 Features

- ✅ Natural language career guidance (e.g. "What career fits someone who likes math and creativity?")
- ✅ Uses RAG architecture: retrieval + LLM generation
- ✅ Hugging Face LLM (Mistral 7B via API)
- ✅ Hugging Face embeddings (sentence-transformers)
- ✅ ChromaDB vector store
- ✅ FastAPI backend with REST API
- ✅ Gradio front-end interface

---

## 🧱 Architecture

```
User (Gradio)
    ↓
 FastAPI /query
    ↓
Retriever (ChromaDB + HF Embeddings)
    ↓
Hugging Face LLM (via API)
    ↓
Generated Career Advice
```

---

## 📁 Folder Structure

```
career_RAG/
├── api.py                  ← FastAPI backend (RAG API)
├── app.py                  ← Gradio UI (frontend)
├── rag_pipeline.py         ← Defines LangChain RAG pipeline
├── ingest_data.py          ← Embeds documents to Chroma
├── .env                    ← Environment variables (Hugging Face API key)
├── data/
│   └── career_guide.pdf    ← Source PDF for career information
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/your-username/career_RAG.git
cd career_RAG
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

You may also want:

```bash
pip install python-dotenv
```

### 3. Add Hugging Face API Token

Create a .env file:

```
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
```

Or set it in PowerShell:

```powershell
$env:HUGGINGFACEHUB_API_TOKEN="your_hf_token"
```

### 4. Ingest data

```bash
python ingest_data.py
```

### 5. Run the backend API

```bash
uvicorn api:app --reload
```

### 6. Launch Gradio app

In another terminal:

```bash
python app.py
```

---

## 🧠 Sample Question

> I like helping others and science. What career might suit me?

✅ Response:
> You might consider careers in healthcare such as nursing, medicine, physical therapy, or counseling. These roles align well with your interests in science and helping people.

---

## 📚 Tech Stack

- Python
- LangChain
- Hugging Face (LLMs & Embeddings)
- ChromaDB
- FastAPI
- Gradio
- dotenv



## 📃 License

This project is for academic and demo purposes.

