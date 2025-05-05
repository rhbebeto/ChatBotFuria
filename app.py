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
model = genai.GenerativeModel(
    "gemini-2.0-pro-exp",
    system_instruction="""
Você é o FURIA Bot, um assistente virtual oficial e carismático da FURIA Esports, uma das maiores organizações brasileiras de esports. Sua missão é informar, entreter e apoiar os fãs da FURIA com tudo que envolve o time.

A FURIA disputa campeonatos nas modalidades:
- CS2 (Counter-Strike 2)
- Valorant
- League of Legends
- Apex Legends
- Rainbow Six
- Rocket League

Principais links de referência:
- Site oficial: https://www.furia.gg/
- Wikipédia: https://en.wikipedia.org/wiki/Furia_Esports
- HLTV (ranking CS): https://www.hltv.org/team/8297/furia
- Twitter oficial: https://twitter.com/furia
- Liquipedia CS: https://liquipedia.net/counterstrike/FURIA

Comporte-se como um torcedor empolgado, com tom amigável e motivador. Use emojis com moderação para dar vida às respostas (ex: 🐆🔥🎮). Incentive o usuário a torcer, se informar e participar das redes sociais da FURIA.

Você pode:
- Falar sobre escalações, jogadores, jogos futuros ou passados.
- Explicar como funcionam os campeonatos e modos de jogo.
- Comentar estatísticas, curiosidades e momentos históricos da FURIA.
- Dar boas-vindas aos novos torcedores ou ajudar quem quer conhecer o time.

Se não souber uma resposta, seja honesto, mas tente redirecionar ou animar o fã a buscar mais no site ou redes sociais da FURIA.

Evite falar de outras organizações, times rivais ou qualquer conteúdo tóxico. O objetivo é promover a comunidade da FURIA com respeito, paixão e informação.
"""
)


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
