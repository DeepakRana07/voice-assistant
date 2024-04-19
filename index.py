import pyttsx3
import datetime
import  speech_recognition as sr

import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour =int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak(" Good evening")
    
    elif hour>=12 and hour<18:
        speak(" good afternoon")

    else:
        speak(" Good evening")

    speak(" i am robot sir how can i help u deepak sir")  


def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        
        # r.adjust_for_ambient_noise(source)
        audio=r.listen(source,timeout=8,phrase_time_limit=8) 

        print(" i am starting")             

    try:
        print(" recognisation")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:

        # print(e)
        print(" say that aagain please")
        return "None"  
          
    return query  


         
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    print(server)
    server.ehlo()
    server.starttls()
    server.login('youremail','password')
    server.sendmail('senderemail',to,content)
    server.close()

if __name__=="__main__":
    wishme()
    

    while True:
        query=takecommand().lower()
    #logic for executing task

        if 'wikipedia' in query:
           speak("searching wikipedia")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("according to wikipedia")
           print(results)
           speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")     

        elif 'play music' in query:
            music_dir ='C:/Users/DELL/Desktop/songs' 
            songs=os.listdir(music_dir)  
            print(songs) 
            os.startfile(os.path.join(music_dir,songs[0]))  

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"sir the time is {strtime}")  

        elif 'the code' in query:
            codepath='"C:/Program Files (x86)/Dev-Cpp/devcpp.exe"'
        
            os.startfile(codepath)

        elif 'email to deepak' in query:

            try:
                speak(" what should i say?")
                content=takecommand()
                to="youremail" 
                sendEmail(to,content)
                speak(" Email has been sent !") 
            
            except Exception as e:
                print(e)
                speak(" listen boss email can only be delivered when your login credentials ")      
                 