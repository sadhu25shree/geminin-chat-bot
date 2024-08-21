
import streamlit as st
import google.generativeai as genai

st.title("welcome to gemini chat")


genai.configure(api_key="AIzaSyC-6mgizFNSpgYfq4bDNOIt1TN0PAeVaL8")

text = st.text_input("Enter Your Question")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if st.button("Click Me"):
    response = chat.send_message(text)
    st.write(response.text)
