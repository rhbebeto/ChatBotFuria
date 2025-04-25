import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

# Carrega as variáveis do arquivo .env
load_dotenv()

chave_api = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=chave_api)
model = genai.GenerativeModel("gemini-2.0-pro-exp")

# flask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
