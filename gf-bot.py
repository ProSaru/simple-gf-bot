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
        "I miss you": "I miss you too!",
        "I'm sorry": "It's okay, I forgive you.",
        "I'm tired": "You should rest, baby.",
        "I'm bored": "Let's do something fun together!",
        "I'm hungry": "Let's eat something delicious!",
        "I'm sleepy": "Go to bed, baby.",
        "I'm happy": "I'm happy too!",
        "I'm sad": "What's wrong, baby?",
        "I'm mad": "Calm down, baby.",
        "I'm stressed": "Take a deep breath and relax.",
        "I'm excited": "I'm excited too!",
        "I'm worried": "Don't worry, everything will be okay.",
        "I'm sick": "Take care of yourself, baby.",
        "I'm cold": "I'll keep you warm.",
        "I'm hot": "I'll cool you down.",
        "I'm sleepy": "Go to bed, baby.",
        "I'm busy": "Take your time, baby.",
        "I'm free": "Let's spend time together!",
        "I'm here": "I'm here for you, baby.",
        "I'm there": "I'm here for you, baby.",
        "I'm happy": "I'm happy too!",
        "I'm sad": "What's wrong, baby?",
        "I'm mad": "Calm down, baby.",
        "I'm stressed": "Take a deep breath and relax.",
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
