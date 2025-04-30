const userInput = document.getElementById("userInput");
const botao = document.getElementById("botao");


//funcao para enviar o json para o flask
function fazerPost(url, message) {
    console.log(message);
    let request = new XMLHttpRequest();
    request.open("POST", url, true);
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    request.send(JSON.stringify(message));

    request.onload = function () {
        console.log(this.responseText);
        const data = JSON.parse(this.responseText)
        const respostaBot = data.reply;
        const chatBox = document.getElementById("chatBox");
        const botMessage = document.createElement("div");
        botMessage.className = "bot-message";
        botMessage.textContent = respostaBot;
        chatBox.appendChild(botMessage); // Adiciona a mensagem do bot ao chatbox
        // Scroll automático para o final       
        chatBox.scrollTop = chatBox.scrollHeight;



    }
    return request.responseText;
}

//gera o json e chama a funcao de post
botao.addEventListener("click", function () {
    event.preventDefault(); // Prevent the default form submission behavior
    flaskUrl = "http://127.0.0.1:5000/chat";

    const inputText = userInput.value;

    const message = {
        message: inputText
    };

    const chatBox = document.getElementById("chatBox");
    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = inputText;
    chatBox.appendChild(userMessage); // Adiciona a mensagem do usuário ao chatbox
    // Scroll automático para o final
    chatBox.scrollTop = chatBox.scrollHeight;
    // Limpa o campo de input
    userInput.value = "";


    fazerPost(flaskUrl, message);
});