import streamlit as st 
from utills.embedding import text_to_embedding
from utills.chunking import chunking
from utills.completion import generate_completion
from utills.retrieval import load_faiss_index, retrive_chunks
from utills.prompt import build_prompt


st.title("RAG App - Book Chapter Asking")
st.write("Ask questions regarding the books Chapter 12")

query = st.text_input("Enter your questio here")

if query:
    index, chunk_mapping = load_faiss_index()
    top_chunks = retrive_chunks(query,index,chunk_mapping)
    prompt = build_prompt(top_chunks, query)
    response = generate_completion(prompt)

    st.subheader("Answer")
    st.write(response)

    with st.expander("Retrived Chunks"):
        for chunk in top_chunks:
            st.markdown(f"- {chunk}")
