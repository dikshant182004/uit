import pyttsx3 as p
import speech_recognition as sr
import threading

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # adjust for ambient noise
        print("Listening...")

        audio = r.listen(source)

    try:
        # Using the Google Web Speech API for speech recognition
        text = r.recognize_google(audio, language='en')
        
        if text:
            if "with" in text.lower() or "one" in text.lower():
                speak("Sure sir, please enter your ATM PIN.")
            else:
                print("Sorry, I couldn't understand what you said.")
        else:
            print("No speech detected.")

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

engine = p.init()  # initialization
engine.setProperty('rate', 155)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

speak("Hello, I am listening. Please speak.")

r = sr.Recognizer()  # speech recognizer

# Start listening thread
listen_thread = threading.Thread(target=listen)
listen_thread.start()


