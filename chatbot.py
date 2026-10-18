def chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hi there!")
        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm fine, thanks for asking!")
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I am a basic rule-based Python chatbot created for my internship.")
        elif user_input in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'.")

if __name__ == "__main__":
    chatbot()