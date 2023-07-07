import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import livejson
import os, sys
import time as tm
from gtts import gTTS
import requests
import json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 178)
engine.setProperty('voice', voices[1].id)

data = livejson.File("data.json", True, True, 4)


def talk(text):
    try:
        engine.say(text)
        engine.runAndWait()
        print(text)
    except Exception as e:
        print(e)

os.system("cls")

def take_command():
    try:
        tm.sleep(1)
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language="en-US")
            command = command.lower()
            if 'fx' in command:
                command = command.replace('via', '')
    except Exception as e:
        print(e)
    return command

def take_voice():
    try:
        tm.sleep(1)
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except Exception as e:
        print(e)
    return command


def run_via():
    global data
    run_bot = True
    while run_bot == True:
        try:
            command = take_command()
            if command:
                run_bot = 1
        except:
            print("Fail to catch voice commands. if want to using again please 'type via'")
            command = str(input("type commands here => "))
            if command == "via":
                pass
            else:
                run_bot = 1
        if run_bot == 1:
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'find on wiki' in command:
                person = command.replace('find on wiki', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'hi' in command or 'hi via' in command or 'hello' in command:
                if data["owner_name"] == "":
                    talk("We do not know each other")
                    tm.sleep(0.3)
                    talk("what's your name?")
                    name = take_voice()
                    confirm = False
                    while confirm == False:
                        talk("are you name is {}".format(name))
                        confirm_name = take_voice()
                        if confirm_name == "yes":
                            confirm = True
                            data["owner_name"] = name
                            talk("oke.. hi {}".format(data["owner_name"]))
                        elif confirm_name == "no":
                            pass
                        else:
                            talk("sorry i dont understand")
                else:
                    talk("hi {}".format(data["owner_name"]))

            elif 'are you single' in command:
                talk('I am in a relationship with wifi')
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            else:
                talk("i don't understand")


while True:
    try:
        run_via()
        os.execv(sys.executable, ['python'] + sys.argv)
    except:
        os.execv(sys.executable, ['python'] + sys.argv)
