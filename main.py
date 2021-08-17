import sys
import webbrowser as wb
from time import ctime

import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
engine = pyttsx3.init()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that!!")
        except sr.RequestError:
            speak("Network Down")
    return voice_data


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def search():
    query = record_audio("What do you want to search for?")
    url = "https://google.com/search?q=" + query
    speak("Here it is")
    wb.get().open(url)
    return "Have a gud day"


def maps():
    loc = record_audio("Where")
    url = "https://google.nl/maps/place/" + loc
    wb.get().open(url)
    return "Have a gud day"


# def respond(speech):
#     res = {"name": "Baymax", "time": ctime(), "search": search(), "place": maps(), "exit": sys.exit(0)}
#
#     for keyword in res.keys():
#         print(keyword)
#         if keyword in speech:
#             speak(res.get(keyword))
#             break

def respond(speech):
    res = {"name": "Baymax", "time": ctime, "search": search, "place": maps, "exit": sys.exit}
    for keyword, answer in res.items():
        if keyword in speech:
            if callable(answer):
                speak(answer())
            else:
                speak(answer)
            break
    speak("Better Luck next Time")


while 1:
    s2t = record_audio("How can I help You")
    print(s2t)
    respond(s2t)
