import pyttsx3

engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
speak_text('hello, madam')

import pyttsx3
engine = pyttsx3.init()
def speak_text(text):
    engine.say(text)
user_text = input("enter your message : ").lower( )
name = "user"
if "my name is " in user_text:
    name = user_text.split("my name is ")[-1].strip( )
elif "name is " in user_text:
    name = user_text.split("name is ")[-1].strip( )

if user_text in["hi","hello","hey"]:
    response = "Hello ! How can i help u?"
elif "name" in user_text:
    response = f" Hello (name),how can i help u?"
else :
    response = "sorry ,i didnt understand that"
print(response)
speak_text(response)
engine.runAndWait( )
           
              
