import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import cv2

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello I am Alexa")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
      with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print("Recognizing...")

        if "alexa" in command:
             print(command)
        else:
            engine.say("u r not calling Alexa")
            engine.runAndWait()
    except:
        print("Your Microphone is not working properly")
        command="Your Microphone is not working properly"
    return command

def run_command():
    command = take_command()
    if 'alexa' in command:
        command = command.replace('alexa', '')
        if "play song on youtube" in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is' + time)
            print(time)
        elif 'who' in command:
            person = command.replace("who is", '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'notepad' in command:
            npath = 'C:\\WINDOWS\\system32'
            os.startfile(npath)
        elif ' open browser' in command:
            npath = 'C:\\Program Files\\Mozilla Firefox'
            os.startfile(npath)
        elif 'command prompt' in command:
            os.startfile('start cmd')
        elif 'camera' in command:
             ap= cv2.VideoCapture(0)
             while True:
                 ret, img = ap.read()
                 cv2.inshow('webcam',img)
                 k= cv2.waitKey(50)
                 if k==27:
                     break;
             ap.release()
             cv2.destroyAllWindows()
        elif 'creator' in command:
            talk('Himanshu sharma')
        elif 'are you single' in command:
            talk('No I am relationship with my creator')
        elif 'I love you' in command:
            talk('Sorry i have a boyfriend')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())
        elif 'play music' in command:
            music = 'C:\\Users\\Himanshu Sharma\\Music'
            songs = os.listdir(music)
            os.startfile(os.path.join(music,songs[0]))
        else:
            talk("Please say the command again")
while True:
    run_command()

