from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on your custom dataset
trainer.train('C:\Users\anagh\OneDrive\Desktop\chatbot\Dataset.txt')

# You can also train on built-in datasets for general conversation
#trainer.train('chatterbot.corpus.english')

# Save the trained model (optional)
#chatbot.save('mychatbot_model')
