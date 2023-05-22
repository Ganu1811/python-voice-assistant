import webbrowser
import speech_recognition as sr
import pyttsx3


# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)  # Use Google Speech Recognition API
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I could not connect to the speech recognition service.")
        return ""

# Function to speak the response
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Main program loop
while True:
    command = listen()

    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "what is your name" in command:
        speak("My name is ChatGPT. Nice to meet you!")
    elif "goodbye" in command:
        speak("Goodbye!")
        break  # Exit the loop
    elif "open website" in command:
        speak("suere! which website do you want to open")
        website = listen()
        webbrowser.open(website)
    else:
        speak("I'm sorry, I cannot perform that task.")
