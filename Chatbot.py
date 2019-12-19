from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer






chatbot = ChatBot("Kundar")
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)
    
def Chatbotresponse(user_input):
    return chatbot.get_response(user_input)
