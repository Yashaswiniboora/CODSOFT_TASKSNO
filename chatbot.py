print("Welcome to AI Chatbot!")
print("Type 'bye' to exit.\n")
while True:
    user=input("You:").lower()
    if user in ["hello","hi","hey"]:
        print("Bot:Hello! How can I help you ?")
    elif "name" in user:
        print("Bot: I am a Rule-Based AI Chatbot.")
    elif "how are you ?" in user:
        print("Bot:I'm doing great! Thanks for asking.")
    elif "help" in user:
        print("Bot: I can answer simple questions and have a basic conversation.")
    elif user in [ "bye","exit","quit"]:
        print("Bot: GoodBye! Have a nice day!")
        break
    else:
            print("Bot:Sorry,I don't understand that")