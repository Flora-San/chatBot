from Chatbot import Chatbot


class ChatbotController:
    def __init__(self):
        self.chatbot = Chatbot()

    def start_chat(self):
        print("Chatbot: Hi! How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye!")
                break
            response = self.chatbot.get_response(user_input)
            print("Chatbot:", response)
