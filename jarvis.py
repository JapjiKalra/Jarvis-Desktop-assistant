import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else :
        speak("good evening")
    speak("hi im jarvis! how can i help you ?")
    

def takecommand():
    
    #takes mike input from user and returns string output
    
    r = sr.Recognizer()                                      
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio=r.listen(source)
    
    try:
        print("Processing Audio...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User's Command: {query} \n")

    except :
        print("Please Repeat...")
        return "None"
    
    return query

def sendemail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('japjikalra@gmail.com','pswd')
    server.sendmail('japjikalra@gmail.com',to,content)
    server.close()






if __name__=="__main__":
    speak("time to code")
    wishme()
    while True:
        print("users turn")
        query=takecommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'launch udemy' in query:
            webbrowser.open("https://www.udemy.com/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'online gdb' in query:
            webbrowser.open("onlinegdb.com")

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak (f"the time is {strtime}")

        elif 'open code' in query:
            codepath="C:\\Users\\japji\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email me' in query:
            try:
                speak("Drop your message")
                content=takecommand()
                to="japjikalra@gmail.com"
                sendemail(to,content)
                speak("Email sent!")
            except Exception as e:
                print(e)
                speak("Sorry failed to send")
        

        if 'quit' in query:
            exit()



    
        
        
        
        

    
