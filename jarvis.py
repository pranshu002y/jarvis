import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("hello daddy ")


    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("say that again daddy...")
            return "None"
        return statement


def wish():
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak("Hello,Good Morning,daddy")
            print("Hello,Good Morning")
        elif hour >= 12 and hour < 18:
            speak("Hello,Good Afternoon,daddy")
            print("Hello,Good Afternoon")
        else:
            speak("Hello,Good Evening,daddy")
            print("Hello,Good Evening")
        speak("hello daddy ,i am friday ,how can i help you daddy")

               
if __name__ == "__main__":
    
    
    takecommand()
    wish()
    while True:
        query = takecommand().lower()
        if query==0:
           continue
        if "good bye" in query or "ok bye" in query or "stop" in query:
            speak('FRIDAY IS SHUTTING DOWN,Good bye')
            print('FRIDAY IS SHUTTING DOWN,Good bye')
            break
        if "madarchod" in query or "bhosdi ke" in query or "bahan k lode" in query or "ludo" in query:
            speak('nirahi pagal hai ke')
            print('maa chuda')
            
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
            speak("notepad is open now")
            
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitkey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            speak ("camera is open now")
            
        elif "play music" in query:
             music_dir="F:\\ENTERTAINMENT"
             songs = os.listdir(music_dir)
             os.startfile(os.path.join(music_dir, songs[0]))
             speak("music in open now")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            
        elif 'open google' in query:
            speak("what you want to search")
            inputs = takecommand()
            webbrowser.open_new_tab("https://www.google.com/?#q=" +inputs)
            speak("Google chrome is open now")
            
        elif "send message" in query:
            kit.sendwhatsmsg("+9792130019", "this is testing protocol",2,25)
            
        elif "play song on youtube " in query:
            kit.playyt("see you again")
            speak("youtube is open now")

        
        elif 'play'  in query:
            query = query.replace("play", "")
            webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={query}')
            
            
        elif "close google" in query:
            speak("closing google")
            os.system("taskkill /f/im google.exe")

        elif "open instagram " in query or "open tiktok" in query:
            webbrowser.open_new_tab("https://www.instagram.com/")
            speak("instagram is open now")

    
            
        elif "sleep" in query:
            speak("i am sleeping... you can call me anytime")
            break
                   
if __name__=='__main__':
    while True:
        permission = takecommand
        if "activate" in permission:
            speak("i am online sir")
            
        elif "shutdown" in permission:
            speak("i am shutting down")
            break


        
  
