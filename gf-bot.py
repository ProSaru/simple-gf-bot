# Description: A simple chatbot that simulates a girlfriend.

def chatbot_response(user_input):
    responses = {
        "hey": "Hi baby",
        "hello": "Hi baby",
        "Hello": "Hi baby",
        "i love you": "I love you too!",
        "what's up": "Nothing much, just thinking about you.",
        "thanks": "You're welcome!",
        "you're cute": "Aww, thank you!",
        "What are you doing today?": "Thinking about you, as always!",
        "Have you eaten?": "Not yet. Want to eat together?",
        "I love you": "I love you too!",
        "Goodnight": "Sweet dreams!",
        "I miss you": "I miss you too!"
    }
    
    return responses.get(user_input, "I don't quite understand what you mean.")

def chat():
    print("Welcome to the Girlfriend Chatbot. Start a conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "end"]:
            print("Chatbot: Ending the conversation. See you next time!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
