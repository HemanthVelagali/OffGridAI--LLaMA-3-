

import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Please speak something...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        recognized_text = recognizer.recognize_google(audio)
        print(f"Recognized: {recognized_text}")
        return recognized_text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return None

if __name__ == "__main__":
    text = "Hello! I am speaking locally without any API."
    speak(text)

    # Uncomment the following line to test speech recognition
    # recognized_text = recognize_speech_from_mic()
    # if recognized_text:
    #     print(f"You said: {recognized_text}")



