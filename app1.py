import streamlit as st

st.markdown("""
<style>

        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            }
</style>

""",unsafe_allow_html=True)
st.title("Simple Input appp!")


name = st.text_input("Enter your name")
if st.button("Submit"):
    st.write(f"Hello", name)