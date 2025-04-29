const userInput = document.getElementById("userInput");
const botao = document.getElementById("botao");

botao.addEventListener("click", function () {
    inputText = userInput.value;
    console.log(inputText);
});