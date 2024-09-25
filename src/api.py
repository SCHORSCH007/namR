import os
import google.generativeai as genai

def get_api_key():
    api_key = os.getenv('GOOGLE_API_KEY')
    return api_key

def do_request(key:str, content:str):
    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(content)
    cleaned = response.text.strip()
    return cleaned


