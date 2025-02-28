window.onload = function () {
    window.sendMessage = async function sendMessage() {
        let questionInput = document.getElementById("question");
        let question = questionInput.value.trim();
        if (!question) return;

        let chatbox = document.getElementById("chatbox");

        let userMessage = document.createElement("div");
        userMessage.className = "message user";
        userMessage.textContent = question;
        chatbox.appendChild(userMessage);

        questionInput.value = "";

        let response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: question })
        });

        let data = await response.json();

        let botMessage = document.createElement("div");
        botMessage.className = "message bot";
        botMessage.textContent = data.answer;
        chatbox.appendChild(botMessage);
    };
};
