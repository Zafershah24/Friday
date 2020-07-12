import os
import smtpd
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3

print("Initializing JARVIS")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
        engine.say(audio)
        engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else :
        speak("Good Evening")
    speak("I am Jarvis.How may I help you?")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising..")
        query=r.recognize_google(audio,language="en-US")
        print(f"User Said:{query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please..")
        return "None"
    return query

def sendEmail(to,content):
    server =smtpd.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()
    server.login('zafershah247@gmail.com',"your-password")
    server.sendmail('zafershah247@gmail.com',to,content)
    server.close()

if __name__=="__main__":
     wishMe()
     while True:
         query=takeCommand().lower()
         if 'wikipedia' in query:
             speak("Searching in Wikipedia..")
             query=query.replace("Wikipedia","")
             results=wikipedia.summary(query,sentences=3)
             speak("According to Wikipedia")
             speak(results)
         elif 'open youtube' in query:
             webbrowser.open("youtube.com")
         elif 'open twitter' in query:
             webbrowser.open("twitter.com")
         elif 'open facebook' in query:
             webbrowser.open("facebook.com")
         elif 'open github' in query:
             webbrowser.open("github.com")
         elif 'open dribble' in query:
             webbrowser.open("dribble.com")
         elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")
         elif 'open google' in query:
             webbrowser.open("google.com")
         elif 'play music' in query:
             music_dir='D:'
             songs=os.listdir(music_dir)
             os.startfile(os.path.join(music_dir,songs[0]))
         # elif 'the time' in query:
         #     strTime=datetime.datetime.now().strftime("%H:%M:%S")
         #     speak(f"the Time is {strTime}")
         elif 'email to Zafar' in query:
             try:
                 speak("What should i do?")
                 content =takeCommand()
                 to ="zafershah247@outlook.com"
                 sendEmail(to,content)
                 speak("email has been sent")
             except Exception as e:
                 print(e)
                 speak("Sorry Sir,couldnt send Email")

