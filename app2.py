import streamlit as st

st.title("Welcome to basic Streamlit app!")

age = st.slider("Select your age", 1, 100)
city=st.selectbox("Selectyour city", ["Mumbai", "Nashik", "Pune", "Haidrabad", "Delhi", "Bangalore", "Chennai", "Kolkata"])

if st.button("Show Details"):
    st.write(f"Your age is {age}")
    st.write("Your city is", city)