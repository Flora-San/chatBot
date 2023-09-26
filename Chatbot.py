import random


class Chatbot:
    def __init__(self):
        # Define a dictionary of responses
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey!"],
            "how are you": ["I'm good, thanks!", "I'm doing well.", "I'm just a bot, but I'm here to help!"],
            "bye": ["Goodbye!", "See you later!", "Have a great day!"],
            "default": ["I'm not sure how to respond to that.", "Could you please rephrase your question?"]
        }

    def get_response(self, user_input):
        # Normalize user input to lowercase
        user_input = user_input.lower()

        # Check if the user input is in the responses dictionary
        if user_input in self.responses:
            return random.choice(self.responses[user_input])
        else:
            return random.choice(self.responses["default"])
