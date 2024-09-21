import streamlit as st
from nltk.chat.util import Chat, reflections

# Custom CSS styles
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2c3e50;  /* Dark Blue Background */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 20px;
    }
    .stText {
        color: white;
    }
    .stButton>button {
        background-color: #3498db;  /* Blue Button Color */
        color: white;
        border-radius: 5px;
    }
    .stTextArea>div>div>textarea {
        background-color: #2980b9;  /* Dark Blue Textarea */
        color: white;
        border-radius: 5px;
    }
    .user-message {
        background-color: #27ae60;  /* Green User Message */
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: 70%;
        align-self: flex-start;
    }
    .bot-message {
        background-color: #8e44ad;  /* Purple Bot Message */
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: 70%;
        align-self: flex-end;
    }
    .message-label {
        font-weight: bold;
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def chatbot_response(user_input):

    pairs = [
        ["hi|hey|hello|heyya", ["Hello", "Hey there"]],
        ["what is your name ?|what's your name ?|may i know your name ?",
         ["I'm a chatbot and My name is AIsha :), May I know your name!"]],
        ["my name is (.*)", ["Hello %1, How are you today?"]],
        ["i am fine|iam good|iam fine", ["Great to hear that", "Awesome!"]],
        ["how are you ?|how you ?", ["I'm fine"]],
        ["can you crack a joke for me ?|can you say another joke ?|tell a joke",
         ["Let's see, this could be unbelievably funny or absolutely awful!...Why don't some couples go to the gym ?",
          "What movie should you watch on a dinner date ?"]],
        ["why", ["Because, some relationships don't workout >_<"]],
        ["what", ["Kabhie Khushi Kabhi Rum !!"]],
        ["one more please | can you say one more",
         ["Yes sure! What do you call a rose that wants to go to the moon? GULAB JA MOON !!"]],
        ["you are too good | wow", ["Ayyo! Thank you :) | Glad you liked it!"]],
        ["tell me something interesting | share a fun fact", [
            "Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."]],
        ["how's the weather today | tell me the weather", [
            "I'm just a chatbot and don't have real-time information, but you can check a weather website or app for the current weather in your area!"]],
        ["favorite color | what's your favorite color?", [
            "I don't have a favorite color since I'm just a program, but I like the sound of 'electric blue'! What about you?"]],
        ["thank you | thanks | appreciate it",
         ["You're welcome! If you have any more questions or just want to chat, feel free to ask."]],
        ["ok bye | ok i'll leave |bye", ["Bye bye, take care. See you soon :) "]],
    ]


    chatbot = Chat(pairs, reflections)
    return chatbot.respond(user_input)

def main():
    st.title("Chatbot App")

    st.sidebar.markdown("### Chatbot Controls")

    # Initialize session state if not already initialized
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    with st.container():
        st.image("https://cdn.icon-icons.com/icons2/1736/PNG/512/4043251-avatar-female-girl-woman_113291.png", width=200)  # Replace with your logo URL
        st.markdown("<h2 style='color: white;'>Chat with AIsha</h2>", unsafe_allow_html=True)

    conversation_container = st.container()

    with conversation_container:
        conversation_history = st.empty()
        user_input = st.text_input("You:")

        if user_input:
            st.session_state.messages.append(("user", user_input))
            response = chatbot_response(user_input)
            st.session_state.messages.append(("bot", response))

        conversation_history.markdown(
            "<br>".join(
                f'<div class="message-label">{sender.capitalize()}:</div><div class="{sender}-message">{message}</div>'
                for sender, message in st.session_state.messages),
            unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
