from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from transformers import pipeline
import os

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
qa_model = pipeline("text-generation", model="microsoft/phi-2", max_new_tokens=512)

def load_and_index_module(module_name: str, path: str):
    docs = []
    module_path = os.path.join(path, module_name)
    for file in os.listdir(module_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(module_path, file))
            docs.extend(loader.load_and_split(text_splitter))
    vectordb = Chroma.from_documents(documents=docs, embedding=embedding_model, persist_directory=f"db/{module_name}")
    vectordb.persist()
    return vectordb

def answer_question(query: str, module_name: str):
    vectordb = Chroma(persist_directory=f"db/{module_name}", embedding_function=embedding_model)
    relevant_docs = vectordb.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    prompt = f"Answer this based on ServiceNow {module_name} documentation:\n\n{context}\n\nQuestion: {query}"
    response = qa_model(prompt)[0]['generated_text']
    return response
