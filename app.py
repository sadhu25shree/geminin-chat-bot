
import streamlit as st
import google


st.title("welcome to gemini chat")

#generativeai as genai

genai.configure(api_key="AIzaSyC-6mgizFNSpgYfq4bDNOIt1TN0PAeVaL8")

text = st.text_input("enter your question")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if st.button("click me"):
    response = chat.send_message(text)
    st.write(response.text)