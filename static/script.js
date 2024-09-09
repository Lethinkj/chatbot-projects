document.getElementById('chatButton').addEventListener('click', function () {
    document.getElementById('chatBox').classList.add('open');
});

document.getElementById('closeChat').addEventListener('click', function () {
    document.getElementById('chatBox').classList.remove('open');
});

document.getElementById('sendButton').addEventListener('click', function () {
    sendMessage();
});

// Allow pressing Enter to send a message
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault(); // Prevent default Enter key behavior
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === "") return;

    // Append the user's message
    appendMessage(userInput, 'user');

    // Clear the input field
    document.getElementById('userInput').value = "";

    // Send the user's message to the server
    fetch('/chatbot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Append the chatbot's response
        appendMessage(data.response, 'bot');
    })
    .catch(error => {
        // Handle errors and append an error message
        appendMessage("Error: Could not contact the chatbot.", 'bot');
        console.error("Error:", error);
    });
}

function appendMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = message;

    const chatBody = document.getElementById('messages');
    chatBody.appendChild(messageDiv);
    
    // Ensure chatbox scrolls to the bottom
    chatBody.scrollTop = chatBody.scrollHeight;
}
