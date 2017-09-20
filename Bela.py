'''
Projeto de estudo sobre Chatbot
Desenvolvedor: Adriano Santos
a.k.a: Isabela (Bela)
'''

# Módulos utilizados para o funcionamento de Bela.
import pyttsx3
from chatterbot import ChatBot
import speech_recognition as sr

# Cria instâncias
engine = pyttsx3.init('sapi5')
# Cria a instância responsável por reconhecer o que você fala.
r = sr.Recognizer()


# Método responsável pela fala
def speak(speech):
    print ("Bela: ", speech)
    engine.say(speech)
    engine.runAndWait()

chatbot = ChatBot("BelaBot", 
                    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
                    storage_adapter="chatterbot.storage.SQLStorageAdapter",
                    logic_adapters=[
                        {
                            'import_path': 'chatterbot.logic.BestMatch'
                        },
                        {
                            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                            'input_text': 'I need help.',
                            'output_text': 'Ok. Whats happen?.'
                        },
                        {
                            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                            'input_text': 'What is your name?',
                            'output_text': 'Thank you for ask me, my name is Bela.' 
                        },
                        {
                            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                            'threshold': 0.40,
                            'default_response': 'I am sorry, but I do not understand.'
                        }
                    ],
                  database="belaDB.db"
                 )

# Utilizado para o processo de aprendizado.
#chatbot.train('chatterbot.corpus.english')

# Para iniciar a conversa.
speak('Hi! My name is Bela! What can I do for you?')

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    
    while True:
        print ('You: ')
        audio = r.listen(source) #Obtem o audio
        speech = r.recognize_google(audio) # Reconhecimento da fala
        response = chatbot.get_response(speech) # Obtem a resposta de Bela
        speak(response) # Bella responde.
