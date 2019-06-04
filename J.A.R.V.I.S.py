import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
from mss import mss
engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('your_own_ID')

voices = engine.getProperty('voices')

now = datetime.datetime.now()

engine.setProperty('voice', voices[len(voices)-1].id)
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

speak('Hello my name is JARVIS welcome back')
speak('Hello Mr.Your last name')
speak('Please stand by sir, giving you full access')
speak('25%')
speak('50%')
speak('75%')
speak('100%')
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning sir!')
        print("current time")
        print(now)

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon sir!')
        print ("current time")
        print(now)

    if currentH >= 18 and currentH !=0:
        speak('Good Evening sir!')
        print("current time")
        print(now)

greetMe()
def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        r.pause_threshold =  1
        r.adjust_for_ambient_noise(source, duration = 2)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(query + '\n')
        
    except sr.UnknownValueError:
        speak ('Sorry sir I didn\'t get that. Please try the command again')
        query = myCommand()

    return query
    
    
speak ('what is your command?')
if __name__ == '__main__':
    while True:
        query = myCommand();
        query = query.lower()
        if 'open youtube' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            webbrowser.open('www.google.com')

        elif 'open gmail' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            webbrowser.open('www.gmail.com')
            
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            
        elif 'open wikipedia' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            webbrowser.open('https://www.wikipedia.org')
    
        elif 'open my drive' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            webbrowser.open('https://drive.google.com/drive/u/0/my-drive')
            
        elif 'activate lockdown' in query:
            speak('Bye sir, activating the security protocols')
            exit()
            
        elif 'close chrome' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            os.system("taskkill /im chrome.exe /f")
            
        elif 'how are you doing?' in query:
            speak('''I'm great sir''')

        elif 'take screenshot' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            with mss() as sct:
                sct.shot()
                
        elif'open hacksmith' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            webbrowser.open('https://www.youtube.com/channel/UCjgpFI5dU-D1-kh9H1muoxQ')
            
        elif 'play vbs song playlist' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            webbrowser.open('https://www.youtube.com/watch?v=KSURGdQediE&list=RDQMY7R65JS8p_U&start_radio=1')
            
            
        elif 'email' in query:
            speak('who is the recipient?')
            recipient = myCommand()
            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
            
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("email", "password")
                    server.sendmail("email","email" , content)
                    server.close()
                    speak('Email sent!')
                except:
                        speak('Sorry Sir! I am unable to send your message at this moment!')
        
        elif 'open library' in query:
            stMsg1 = ['already on it sir','yes sir','whatever you say sir']
            speak(random.choice(stMsg1))
            path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
            sys.path.append(path)
            import subprocess
            subprocess.Popen('explorer "C:\temp"')
            
        elif 'what is the time' in query:
            speak(now)
        else:
                query = query
                speak('Searching...')
                try:    
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak('Got it.')
                        speak(results)
                    
                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak('Got it.')
                        speak(results)
        
                except:
                    webbrowser.open('www.google.com')
   
        speak('Next Command! Sir!')

