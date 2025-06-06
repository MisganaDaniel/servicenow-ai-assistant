import streamlit as st
from rag_engine import load_and_index_module, answer_question

MODULES = ["ITSM", "CSM"]

st.title("🧠 ServiceNow AI Assistant")
st.markdown("Ask your question based on a selected ServiceNow module.")

module = st.selectbox("Select a ServiceNow Module", MODULES)

if st.button("Index Selected Module"):
    with st.spinner(f"Indexing documents for {module}..."):
        load_and_index_module(module, "modules/")
    st.success(f"{module} indexed successfully!")

query = st.text_input("Ask a question:")
if query:
    with st.spinner("Generating answer..."):
        answer = answer_question(query, module)
    st.markdown("### 💡 Answer")
    st.write(answer)
