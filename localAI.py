import os
import webbrowser
import pyttsx3
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import json

# Voice output
engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

# Load offline model
model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    data = audio.get_raw_data(convert_rate=16000, convert_width=2)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        return result.get("text", "")
    return ""

def open_app(command):
    if "calculator" in command:
        os.system("calc")
        speak("Opening calculator")

    elif "notepad" in command:
        os.system("notepad")
        speak("Opening notepad")

    elif "command prompt" in command:
        os.system("cmd")
        speak("Opening command prompt")

    else:
        speak("Application not found")

def process_command(command):
    print("You:", command)

    if "hello" in command:
        speak("Hello, how can I help you")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open" in command:
        open_app(command)

    elif "exit" in command or "quit" in command:
        speak("Goodbye")
        exit()

    else:
        speak("Sorry, I didn't understand")

def main():
    speak("Offline voice assistant activated")
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
