import brain

def chat():
    print("Welcome to SmartBot! (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        intent = brain.find_intent(user_input)
        response = brain.get_response(intent)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()
