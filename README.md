# ServiceNow AI Assistant (Local + Free)

## Features
- Select module (ITSM, CSM)
- Ask natural language questions
- Get answers from local documentation (no OpenAI)
- Powered by `Phi-2` model (fast and CPU-friendly)

## Getting Started

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Folder Structure

- `modules/`: Put your ServiceNow docs here (per module)
- `rag_engine.py`: Core RAG logic
- `app.py`: Streamlit UI
