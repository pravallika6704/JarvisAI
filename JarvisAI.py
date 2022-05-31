import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voice',voices[0].id)

def speak(audio):
   
    Assistant.say(audio)
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing......")
            query = command.recognize_google(audio,language='en-in')
            print(f"You said : {query}")
        
        except Exception as Error:
            print("say that again")
            return "none"

        return query.lower()

query = takecommand()

if "hello" in query:
    speak("hello sir")
else:
    speak("no command found")

