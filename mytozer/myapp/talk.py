import pyttsx3
from pyttsx3 import engine
def talkk(string):
    engine=pyttsx3.init()
    engine.say(string)
    engine.runAndWait()
    