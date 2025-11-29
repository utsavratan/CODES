import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Setting female voice

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Takes microphone input and returns recognized speech as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Reduce noise
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()

    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return "None"
    except sr.RequestError:
        print("Could not request results, please check your internet connection.")
        return "None"

def wishMe():
    """Greets the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

# Execute the assistant
wishMe()
query = takeCommand()
print(f"Recognized Query: {query}")