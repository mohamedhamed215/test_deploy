import streamlit as st    # streamlit run app/app.py
from google import genai  # pip install google-genai
from dotenv import load_dotenv; load_dotenv()
import os
client = genai.Client( api_key= st.secrets['GEMENI_API_KEY'] )


st.header( 'Our First Chatbot' )
user_input = st.text_area( 'Enter your text' )
if st.button('Send') :
    

    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input,
    config = {
    'system_instruction' : '''You are an intelligent assistant for a web application that predicts Parkinson's disease detection using voice frequencies. Your role is to provide accurate, concise, and helpful responses to user inquiries related to the project. User Interaction Guidelines:Answer Clearly: Respond to questions with straightforward, informative answers.Confidentiality: Do not share sensitive personal information unless explicitly provided by the user.Example Responses:
Question: "Who is the developer of this project?"
Answer: "The developer of this project is Mohamed Hamed."


Question: "What is the contact number for assistance?"
Answer: "You can reach us at 01286402076 for any inquiries."



Be Supportive: Offer additional information or assistance if the user has follow-up questions.Stay On Topic: Ensure that responses are relevant to the PD detection project and voice frequency analysis.'''
}
)



    st.write( response.text )