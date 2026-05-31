import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()

def get_gemini():
    return ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature=0
    )

def get_groq():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )