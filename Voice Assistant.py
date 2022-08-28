import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sytext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing")
            data=recognizer.recognize_google(audio)

            return data

        except sr.UnknownValueError:
            print("Not Understanding")

def speech_text(x):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()


if __name__:= '__main__':
    if sytext().lower() == "hello" :
            while True:


                    data1= sytext().lower()
                    if "your name" in data1:
                        name="TU motaa AAHE"
                        speech_text(name)

                    elif "old are you" in data1:
                        age="i am one year old"
                        speech_text(age)

                    elif "now time" in data1:
                        time=datetime.datetime.now().strftime("%I%H%p")
                        speech_text(time)

                    elif "youtube" in data1:
                        webbrowser.open("https://youtube.com/")

                    elif "jokes" in data1:
                        joke=pyjokes.get_joke(language="en",category="neutral")
                        speech_text(joke)
                        print(joke)

                    elif "play song" in data1:
                        add="C:/Users/DHANASHRI/Desktop/Desktop Cutpaste/papa songs/God/God"
                        listsong=os.listdir(add)
                        print(listsong)
                        os.startfile(os.path.join(add,listsong[0]))

                    elif "exit" in data1:
                        print("Thanks Saurabh")
                        break
                    time.sleep(5)

    else:

        print("AE TU JA RE")