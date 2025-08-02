import os 
from dotenv import load_dotenv
from google import generativeai as genai 

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_completion(prompt,model="gemini-2.5-flash"):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name=model)
    response = model.generate_content(
        contents = prompt
    )
    return response.text
