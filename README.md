## 🐆 FURIA Chatbot

Um chatbot interativo que fornece informações sobre a FURIA Esports, construído com Flask no backend e HTML/CSS/JavaScript no frontend. Utilizando o modelo Gemini da Google, ele responde a perguntas sobre a equipe, seus jogadores, modalidades e próximos eventos, mantendo um tom amigável e direcionado aos fãs.

---

## 🚀 Funcionalidades

- **Informações sobre a equipe**: história, conquistas e modalidades disputadas (CS2, Valorant, LoL, Apex, R6, Rocket League).  
- **Detalhes dos jogadores**: perfil, estatísticas e curiosidades.  
- **Próximos jogos**: datas, adversários e links para fontes oficiais.  
- **Conversas dinâmicas**: respostas geradas pelo Gemini conforme o prompt do sistema.  
- **Histórico de chat**: exibição das últimas mensagens do usuário e do bot, com scroll interno na caixa de mensagens.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.8+** & **Flask** para API RESTful  
- **google-generativeai** (Gemini) para geração de respostas inteligentes  
- **HTML5, CSS3, JavaScript** para interface  
- **Bootstrap** (opcional) para estilos rápidos  

---

## 🛠️ Instalação e Execução

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/seu-usuario/furia-chatbot.git
   cd furia-chatbot

2. **Crie e ative um ambiente virtual**
python -m venv venv
Linux/macOS:
source venv/bin/activate
Windows:
venv\Scripts\activate

3. **Instale as dependências**
pip install -r requirements.txt

4. **Configure a chave da API Gemini**
Crie um arquivo .env na raiz com:
- GEMINI_API_KEY=SuaChaveAqui
- Execute o servidor
- python app.py
- Acesse no navegador
- Abra http://127.0.0.1:5000

