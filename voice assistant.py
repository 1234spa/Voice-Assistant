import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',180)
    engine.say(x)
    engine.runAndWait()
speechtx("hello")

if __name__ == '__main__':
    
    
    if "peter" in sptext().lower():
        while True:
            data1= sptext().lower()
            if "what is your name" in data1:
                name = "my name is peter"
                speechtx(name)
            elif "old are you" in data1:
                age = "i am 2 year old"
                speechtx(age)
            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'google' in data1:
                webbrowser.open("https://www.google.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language= "en",category="neutral")
                speechtx(joke_1)
            elif 'play movies' in data1:
                add= "F:\movies"
                listmovie = os.listdir(add)
                print(listmovie)
                os.startfile(os.path.join(add,listmovie[]))
            elif "exit" in data1:
                speechtx("thank you")
                break
            time.sleep(5)
    else:
        print("thanks")        
    