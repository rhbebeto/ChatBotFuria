
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

chave_api = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=chave_api)

model = genai.GenerativeModel("gemini-2.0-pro-exp")
response = model.generate_content("Voce perecbe que está sendo usa como api?")
print(response.text)
