while True:
    user_input = input("You: ")
    response = train.get_response(user_input)
    print("Bot:", response)
