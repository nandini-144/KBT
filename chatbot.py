import streamlit as st

st.title("Chatbot App")

question = st.text_input("Ask a question to the chatbot:")

if st.button("Get Answer"):
    st.write("you asked:", question)
    st.write("Chatbot is on the process of answering your question...")