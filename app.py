import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

# Carrega as variáveis do arquivo .env
load_dotenv()

chave_api = os.getenv("GEMINI_API_KEY")

if not chave_api:
    raise ValueError(
        "A chave da API não foi encontrada. Verifique o arquivo .env.")

genai.configure(api_key=chave_api)
model = genai.GenerativeModel("gemini-2.0-pro-exp")

# flask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Mensagem não pode ser vazia."}), 400
    # Respostas personalizadas para os fãs da FURIA
    user_message_lower = user_message.lower()

    # Usa a Gemini API para respostas gerais
    try:
        response = model.generate_content(user_message)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Desculpe, algo deu errado: {str(e)}"

    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
