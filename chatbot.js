document.addEventListener("DOMContentLoaded", function () {
    const chatBox = document.getElementById("chatBox");
    const userInput = document.getElementById("userInput");

    function appendMessage(text, className) {
        let messageDiv = document.createElement("div");
        messageDiv.className = className;
        messageDiv.innerText = text;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function getBotResponse(userMessage) {
        userMessage = userMessage.toLowerCase();

        if (userMessage.includes("stress") || userMessage.includes("anxiety")) {
            return "I'm sorry to hear that you're feeling this way. Try some deep breathing exercises or take a short break. Would you like some relaxation tips?";
        } else if (userMessage.includes("exam") || userMessage.includes("study")) {
            return "Exams can be stressful! Remember to take breaks, stay hydrated, and organize your study material. Do you need study tips?";
        } else if (userMessage.includes("sleep")) {
            return "Sleep is crucial for your mental health. Try to maintain a regular sleep schedule and avoid screens before bedtime.";
        } else if (userMessage.includes("sad") || userMessage.includes("depressed")) {
            return "I'm here for you! Talking to someone you trust can help. Would you like to see some motivational quotes?";
        } else {
            return "I'm here to support you. You can talk to me about stress, exams, sleep, or anything on your mind.";
        }
    }

    window.sendMessage = function () {
        let userMessage = userInput.value.trim();
        if (userMessage === "") return;

        appendMessage(userMessage, "user-message");
        userInput.value = "";

        setTimeout(() => {
            let botResponse = getBotResponse(userMessage);
            appendMessage(botResponse, "bot-message");
        }, 500);
    };

    window.handleKeyPress = function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    };
});



