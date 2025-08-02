from google import generativeai as genai
import os 
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def text_to_embedding(text):
    genai.configure(api_key=GEMINI_API_KEY)

    response = genai.embed_content(
        model="gemini-embedding-001",
        content=text
    )

    emb = response['embedding']
    print(emb)
    return emb