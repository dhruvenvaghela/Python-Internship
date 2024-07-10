import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    global command
    try:
        with sr.Microphone() as source: 
            print("Listening...") 
            listener.adjust_for_ambient_noise(source) 
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except :
        return 'not working'

    return command


def run_jarvis():
    cmd = take_command()
    if 'hello jarvis' in cmd:
        cmd = cmd.replace('hello jarvis','')
        print(cmd)
        if "play" in cmd:
            song = cmd.replace("play","")
            talk("playing" + song)
            pywhatkit.playonyt(song)

        elif "time" in cmd:
            time  = datetime.datetime.now().strftime("%I:%M %p")
            talk("current time is "+ time)

        elif "who is" in cmd:
            person = cmd.replace("who is ","")
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif "joke" in cmd:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        else:
            talk("please say the command again.")
    else:
        pass

while True:
    run_jarvis()