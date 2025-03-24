import ollama
from murf import Murf
import requests
import os
from dotenv import load_dotenv
load_dotenv

# Initialize Murf client
MURF_API_KEY = ""
murf_client = Murf(api_key=MURF_API_KEY)

# Store conversation history
conversation_history = []

def speak_with_murf(text):
    """Generate speech using Murf and play the audio."""
    try:
        response = murf_client.text_to_speech.generate(
            text=text,
            voice_id="en-IN-eashwar"
        )

        if response.audio_file:
            # Download the audio file
            audio_url = response.audio_file  # This is a URL
            audio_file = "response.mp3"
            
            audio_data = requests.get(audio_url)
            with open(audio_file, "wb") as f:
                f.write(audio_data.content)

            # Play the downloaded audio file
            os.system(f"start {audio_file}")  # Windows
        else:
            print("Error: No audio file received from Murf.")
    
    except Exception as e:
        print(f"Error with Murf API: {e}")

def chat_with_llama(user_input):
    global conversation_history

    conversation_history.append({"role": "user", "content": user_input})
    response = ollama.chat(model="llama3.1:8b", messages=conversation_history)

    ai_reply = response["message"]["content"]
    print(f"AI: {ai_reply}")

    conversation_history.append({"role": "assistant", "content": ai_reply})
    
    speak_with_murf(ai_reply)  # Convert AI response to speech

    return ai_reply

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break
    chat_with_llama(user_input)
