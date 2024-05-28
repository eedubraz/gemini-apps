from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Loading all environment variables
load_dotenv()

# Setup google genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")

# Function to get responses from Gemini Pro Model
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

# Initialize out streamlite app
st.set_page_config(page_title='Q&A Demo')
st.header('Gemini LLM Aplication')

input=st.text_input('Input: ', key='input')
submit=st.button('Ask the question')

# When submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)