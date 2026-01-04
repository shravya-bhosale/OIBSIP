import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
from gtts import gTTS
from playsound import playsound
import os


def speak(text):
    print("SPEAKING:", text)
    tts = gTTS(text=text, lang="en")
    tts.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand")
        return ""

# Greet user
speak("Hello Shravya, I am your voice assistant. How can I help you?")

while True:
    query = take_command()
    query = query.lower()
    if query == "":
        continue

    if "time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print("TIME:", time)
        speak(f"The time is {time}")

    elif "google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
        
    elif "stop" in query or "exit" in query:
        speak(" Yes,Goodbye!")
        break
