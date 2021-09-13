import pyttsx3 #text-to-speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os #system files
import smtplib #send mail
import random #random nos.
import cv2 #openCV

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('hello there! good morning ')
    elif hour>=12 and hour<17:
        speak('hello there! good afternoon ')
    else :
        speak('hello there! good evening ')
    speak(" i am Falcon . How can i help you")

def microinput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        print('listening....')
        # r.energy_threshold=700
        audio=r.listen(source)

    try:
        print('recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print(f'user said : {query} \n')
        if 'yes' in query :
            speak('searching ....')
            print('searching....')

    except Exception as e:
        # print(e)
        speak('can you please speak up....')
        print('can you please speak up....')
        return "None"
    return query

def sendmail(to,content):
    server=smtplib.SMTP('smpt.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.login('amazinganirudhhere@gmail.com','ok')
    server.sendmail('amazinganirudhhere@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    greet()
    while True:
        query=microinput().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            search=query.replace('youtube' and 'search for','')
            speak("opening youtube in browser")
            webbrowser.open(f'https://www.youtube.com/results?search_query={search}')

        elif 'open google' in query:
            speak("opening google in browser")
            webbrowser.open('www.google.com')

        elif 'gaana' in query or 'ghana' in query or 'gana' in query:
            search=query.replace('in gaana'and'play'and 'gana' and 'ghana','')
            speak("opening gaana in browser")
            webbrowser.open(f'https://gaana.com/search/{search}')

        elif 'open facebook' in query:
            speak("opening facebook in browser")
            webbrowser.open('www.facebook.com')


        elif 'open instagram' in query:
            speak("opening instagram in browser")
            webbrowser.open('www.instagram.com')

        elif 'open twitter' in query:
            speak("opening twitter in browser")
            webbrowser.open('www.twitter.com')

        elif 'open pinterest' in query:
            speak("opening pinterest in browser")
            webbrowser.open('www.pinterest.com')

        elif 'open github' in query:
            speak("opening github in browser")
            webbrowser.open('www.github.com')

        elif 'open gmail' in query:
            speak("opening gmail in browser")
            webbrowser.open('www.gmail.com')

        

        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'the time is {time}')
            print(time)

        elif 'command prompt' in query:
            speak("opening command prompt")
            path="C:\\Windows\\system32\\cmd.exe"
            os.startfile(path)

        elif 'vs code' in query:
            speak("opening visual studio code")
            path="C:\\Program Files\\Microsoft VS Code\\code.exe"
            os.startfile(path)

        elif 'my computer' in query:
            speak("opening My computer")
            path="C:\\Users\\Anirudh\\Desktop"
            os.startfile(path)

        elif 'open pictures' in query:
            speak("opening pictures")
            path="C:\\Users\\Anirudh\\pictures"
            os.startfile(path)

        elif 'open videos' in query:
            speak("opening videos")
            path="C:\\Users\\Anirudh\\videos"
            os.startfile(path)

        elif 'open games' in query:
            speak("opening games")
            path="C:\\Users\\Anirudh\\saved games"
            os.startfile(path)

        elif 'open downloads' in query:
            speak("opening downloads")
            path="C:\\Users\\Anirudh\\Downloads"
            os.startfile(path)

        elif 'search' in query:
            statement=query.replace('search for', '')
            webbrowser.open(statement)

        elif 'shut down' in query or 'shutdown' in query:
            os.system('shutdown -s -t 10')
            
        elif 'restart' in query:
            os.system('shutdown -r -t 10')

        elif 'camera' in query:
            cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
            if not (cap.isOpened()):
                speak('could not open camera')
            while(True):
                ret,frame=cap.read()
                cv2.imshow('Falcon',frame)
                if cv2.waitKey(1)& 0xFF == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    break
            # webbrowser.open(query)

        elif 'email' in query:
            speak("sending email")
            try:
                speak('what should i mail ?')
                content=microinput()
                to='anirudhsk30@gmail.com'
                sendmail(to,content)
                speak('email sent successfully!!')
            except Exception as e:
                print(e)
                speak('unable to send email now !!')
                print('email was not sent')

        elif "what\'s up" in query or 'how are you' in query:
            Msgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            speak(random.choice(Msgs))

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            
        elif "your name"  in query:
            speak('my name is falcon')

        elif 'exit' in query:
            speak("have a great day!!")
            exit()
