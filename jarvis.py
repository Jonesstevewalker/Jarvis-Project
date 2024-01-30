import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os 
import comtypes.client

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def  wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour < 4:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak('I am Happy. Please tell me how can I help you?')

def takeCommand():
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
        
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic of the program will be here
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('openning youtube')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
            speak('openning google')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            speak('openning stackoverflow')

        elif 'open whatsapp' in query:
            webbrowser.open('whatsapp.com')
            speak('openning whatsapp')
        
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
            speak('openning instagram')
        
        elif 'open amazon' in query:
            webbrowser.open('amazon.com')
            speak('openning amazon')
        
        elif 'open flipkart' in query:
            webbrowser.open('flipkart.com')
            speak('openning flipkart')
        
        elif 'open spotify' in query:
            webbrowser.open('spotify.com')
            speak('openning spotify')
        
        elif 'open x' in query:
            webbrowser.open('x.com')
            speak('openning x')
        
        elif 'open hotstar' in query:
            webbrowser.open('hotstar.com')
            speak('openning hotstar')
        
        elif 'open netflix' in query:
            webbrowser.open('netflix.com')
            speak('openning netflix')
        
        elif 'open prime video' in query:
            webbrowser.open('primevideo.com')
            speak('openning primevideo')
        
        elif 'open pinterest' in query:
            webbrowser.open('pinterest.com')
            speak('opening pinterest')

        elif 'open gmail' in query:
            webbrowser.open('mail.google.com')
            speak('opening gmail')

        elif 'play music' in query:
            music = 'D:\songs'
            song = os.listdir(music)
            print(song)
            os.startfile(os.path.join(music,song[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")
