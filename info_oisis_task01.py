import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# Text-to-speech setup
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            command = recognizer.recognize_google(audio)
            print("You:", command)

            return command.lower()

        except sr.UnknownValueError:
            speak("Sorry, I could not understand you. Please repeat.")
            return ""

        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""

        except sr.RequestError:
            speak("Sorry, the speech recognition service is unavailable.")
            return ""


def tell_date_time():
    now = datetime.datetime.now()

    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%A, %d %B %Y")

    speak(f"The current time is {current_time}")
    speak(f"Today is {current_date}")


def web_search(command):
    search_query = command.replace("search for", "").strip()

    if search_query:
        speak(f"Searching for {search_query}")
        url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
        webbrowser.open(url)
    else:
        speak("Please tell me what you want to search for.")


def main():

    speak("Hello! I am your voice assistant. How can I help you?")

    while True:

        command = listen()

        if command == "":
            continue

        # Hello
        if "hello" in command or "hi" in command:
            speak("Hello! Nice to talk to you.")

        # Time/date
        elif "time" in command or "date" in command:
            tell_date_time()

        # Web search
        elif "search for" in command:
            web_search(command)

        # Exit
        elif "exit" in command or "stop" in command or "goodbye" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I don't know that command yet.")


main()