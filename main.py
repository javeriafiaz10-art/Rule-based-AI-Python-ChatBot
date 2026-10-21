#Rule based AI Python ChatBot

import datetime
import time
name = input("Welcome: please enter your name")
currenttime = datetime.datetime.now().hour
if 5 <= currenttime <= 11:
    print("Good Morning" , name)
elif 11 <= currenttime <= 17:
    print("Good afternoon" , name)
elif 17 <= currenttime <= 20:
    print("Good evening",name)
else:
    print("Good Night" , name)         

    


print("ASSALAM U ALAIKUM ! Welcome to AI Personal Assistant ChatBot")
print("You can ask me basics Questions, type 'bye' to exit from ChatBot")

# Creation of Memory of chatbot [dictionay of responses] 
responses = {
    "hello": "Hello! How can I help you?",
    "how are you": "I am fine, thank you!",
    "what is your name": "I am your personal AI assistant.",
    "who created you": "I was created using Python.",
    "what can you do": "I can answer simple questions and assist you.",
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is your purpose": "My purpose is to help you with your questions.",
    "thank you": "You are welcome!",
    "good morning": "Good morning! Have a wonderful day.",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! What can I do for you?",
    "bye": "Goodbye! Have a nice day.",
    "exit": "Goodbye! See you again."
}
#make function
def getresponseBot(userquestions):
    userquestions = userquestions.lower()
    for eachkey in responses:
        if eachkey in userquestions:
            return responses[eachkey]
    return "I am not able to tell yet"        
#user input 
while True:
    userinput = input("Please ask your Question: ")
    reply = getresponseBot(userinput)
    print("Bot Respones" , reply)
    if "bye" in userinput.lower():
        break
