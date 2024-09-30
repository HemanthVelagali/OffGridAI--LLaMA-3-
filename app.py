

from flask import Flask, request, jsonify, send_from_directory, Response
import os
from langchain.llms import Ollama
import speech_recognition as sr  # Import the speech recognition library

# Flask app setup
app = Flask(__name__)

# Global variable to hold the LLaMA 3 model
llama_llm = None

# Function to load the LLaMA 3 model using Langchain
def load_model():
    global llama_llm
    if llama_llm is None:
        try:
            print("Loading LLaMA 3 model...")
            llama_llm = Ollama(model='llama3')  # Specify your model name here
            print("LLaMA 3 model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")

# Function to chat with the model (Normal, single response)
def chat_with_model(user_input):
    if llama_llm is None:
        print("Model is not loaded.")
        return "Model is not loaded. Please start the model."

    try:
        # Get the model's single response
        response = llama_llm(user_input)
        if response:
            return response.strip()
        else:
            return "No response from LLaMA 3."
    except Exception as e:
        print(f"Error during communication: {e}")
        return "Error communicating with LLaMA 3."

# Function to stream response from the model
def stream_model_response(user_input):
    if llama_llm is None:
        return "Model is not loaded. Please start the model."
    
    try:
        # Stream the model's response
        for chunk in llama_llm.stream(user_input):
            yield chunk
    except Exception as e:
        print(f"Error during streaming: {e}")
        yield "Error communicating with LLaMA 3."

@app.route('/')
def serve_html():
    return send_from_directory(os.getcwd(), 'index.html')

# New route for streaming responses
@app.route('/stream-chat', methods=['POST'])
def stream_chat_endpoint():
    user_input = request.json.get('input')
    print(f"User input for streaming: {user_input}")  # Log user input
    return Response(stream_model_response(user_input), content_type='text/event-stream')

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    user_input = request.json.get('input')
    print(f"User input: {user_input}")  # Log user input
    response = chat_with_model(user_input)
    print(f"LLaMA 3 response: {response}")  # Log model response
    return jsonify({'response': response})

@app.route('/stop', methods=['POST'])
def stop_model():
    global llama_llm
    if llama_llm:
        llama_llm = None  # Reset the model instance
        print("LLaMA 3 model stopped.")
        return jsonify({'response': "LLaMA 3 model stopped."})
    return jsonify({'response': "Model was not running."})

@app.route('/reload', methods=['POST'])
def reload_model():
    load_model()
    return jsonify({'response': "LLaMA 3 model reloaded."})

# New route for audio transcription
@app.route('/transcribe-audio', methods=['POST'])
def transcribe_audio():
    recognizer = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)  # Listen for audio input
        print("Transcribing audio...")
        try:
            transcription = recognizer.recognize_google(audio)  # Transcribe the audio using Google Web Speech API
            print(f"Transcription: {transcription}")
            return jsonify({'transcription': transcription})
        except sr.UnknownValueError:
            return jsonify({'transcription': 'Could not understand audio'})
        except sr.RequestError as e:
            return jsonify({'transcription': f'Could not request results; {e}'})

if __name__ == '__main__':
    load_model()  # Load the model when the server starts
    app.run(debug=True, use_reloader=False)

