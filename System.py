import openai
import speech_recognition as sr
import os
from gtts import gTTS
import subprocess
# Set up your OpenAI API key
openai.api_key = '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'

r = sr.Recognizer()

def app(name):


    # The name of the application (e.g., "notepad.exe" for Notepad)
    app_name = name+".exe"

    try:
        subprocess.Popen([app_name])
    except FileNotFoundError:
        print(f"{app_name} not found in PATH or is not an executable file.")

def google(query):

    # Replace this with the path to your Chrome executable
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    # The URL you want to open in Chrome
    url = query

    # Construct the command to open Chrome with the URL
    command = [chrome_path, url]

    # Use subprocess to run the command
    subprocess.Popen(command)


def talk(text):
    # Text you want to convert to speech
    text = text

    # Initialize gTTS
    tts = gTTS(text)

    # Save the speech to a file (you can use other formats like 'mp3' or 'ogg')
    tts.save("output.mp3")

    # Play the saved speech using the default media player
    os.system("start output.mp3")

def record_text():
    while(1):
        try:
            with sr.Microphone() as scource2:

                r.adjust_for_ambient_noise(scource2, duration = 0.2)

                print("I'm listening")

                audio2 = r.listen(scource2)

                MyText = r.recognize_google(audio2)

                MyText = (MyText)
                return MyText
                
    
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    
        except sr.UnknownValueError:
            print("unknown error occured")


def chat_with_jarvis(user_input):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=200  # Adjust as needed
    )
    return response.choices[0].text

print("Hello, I'm your AI assistant. How can I assist you today?")
response = chat_with_jarvis("Can you please act like Jarvis?")
while True:
    user_input = record_text()
    print(user_input)
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    elif user_input.lower() == "search":
        print("Listening")
        user_input = record_text()
        google(user_input)
    elif user_input.lower() == "open":
        print("Listening")
        user_input = record_text()
        user_input = user_input.lower()
        app(user_input)
    else:
        response = chat_with_jarvis(user_input)
        talk(response)
        print(response)