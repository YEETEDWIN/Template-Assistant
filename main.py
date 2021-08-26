import speech_recognition as speech
import pyttsx3
import pywhatkit
import pyjokes
import datetime

listener = speech.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def use_command():
    try:
        with speech.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command


while True:
    command = use_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'search for' in command:
        search_term = command.split("for")[-1]
        pywhatkit.search(search_term)
    elif 'search on youtube' in command:
        search_term = command.split("youtube")[-1]
        pywhatkit.playonyt(search_term)
    else:
        speak('Please say the command again.')
