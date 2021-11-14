import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Friday Sir. Please tell me how may I help you")


def takeCommand():  # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        # print(e)
        print("Say that again please.......")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password') #youremail-- enter your email , password-- enter your email password
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "google" in query:
            webbrowser.open("google.com")

        elif "stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "scratch" in query:
            webbrowser.open("https://scratch.mit.edu/")

        elif "binge watch" in query:
            webbrowser.open("ww7.soap2dayto.org")

        elif "play music" in query:
            music_dir = ''   #enter the path of your music directory
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir ,The time is {strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\HARSHITA JAIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "chrome" in query:
            appPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(appPath)

        elif "jet brains" in query:
            charmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe"
            os.startfile(charmPath)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'youremail@gmail.com'  # youremail -- enter the email message will be sent to
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry unable to sen the email!")

        elif "quit the system" in query:
            speak("Quitting the system")
            break
