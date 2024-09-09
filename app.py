from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Expanded set of responses with clear and simple answers
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! What can I do for you today?",
    "how are you": "I'm just a chatbot, but I'm here and ready to help you!",
    "what is your name": "I'm ChatBot, your virtual assistant. How can I assist you?",
    "bye": "Goodbye! Have a wonderful day!",
    "what is your purpose": "My purpose is to assist you with information and answer your questions.",
    "how can I contact support": "You can contact support by emailing support@example.com or calling 123-456-7890.",
    "what time is it": "I can't check the time, but you can easily find it on your device.",
    "what is the weather like": "I can't provide current weather updates. Please check a weather website or app.",
    "tell me a joke": "Sure! Why did the scarecrow win an award? Because he was outstanding in his field!",
    "what is your favorite color": "I don't have personal preferences, but many people like blue!",
    "where are you located": "I exist in the cloud, so I'm available wherever you are!",
    "what can you do": "I can help answer questions, provide information, and assist with various tasks.",
    "help": "I’m here to help! You can ask me about my features, how to contact support, or just chat with me.",
    "thank you": "You're welcome! If you have any more questions, just let me know.",
    "who created you": "I was created by a team of developers to help with answering questions and providing information.",
    "what is ai": "Artificial Intelligence (AI) is technology that allows machines to mimic human intelligence and behavior.",
    "what are your capabilities": "I can answer general questions, provide information, and help with basic tasks. Feel free to ask me anything!",
    "can you play music": "I can't play music, but I can help you find information about your favorite songs or artists.",
    "how do I reset my password": "To reset your password, please follow the instructions on the password reset page of the website.",
    "where can I find the user manual": "You can find the user manual on our website under the 'Support' section.",
    "how do I change my account settings": "Log in to your account and navigate to the 'Account Settings' section to make changes.",
    "what is the latest news": "I don't have access to real-time news, but you can check news websites or apps for the latest updates.",
    "how can I improve my productivity": "Consider creating a schedule, setting goals, and minimizing distractions to boost your productivity.",
    "how do I contact customer service": "You can contact customer service through email at support@example.com or by calling 123-456-7890.",
    "what is the best way to learn programming": "Practice regularly, take online courses, and work on projects to enhance your programming skills.",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_query = request.json.get('query').strip().lower()
    bot_response = responses.get(user_query, "Sorry, I didn't understand that. Can you please rephrase your question?")
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
