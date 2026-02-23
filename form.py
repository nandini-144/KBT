import streamlit as st

st.title("User Information Form")

# Create a form
with st.form("my_form"):  # give the form a unique name
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=120)
    email = st.text_input("Enter your email")
    gender = st.radio("Select your gender", ["Male", "Female", "Other"])
    
    # Form submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.success("Form Submitted Successfully!")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Email:** {email}")
        st.write(f"**Gender:** {gender}")