import ollama

# Store conversation history
conversation_history = []

def chat_with_llama(user_input):
    global conversation_history

    # Append user input to history in proper format
    conversation_history.append({"role": "user", "content": user_input})

    # Generate response from LLaMA
    response = ollama.chat(model="llama3.1:8b", messages=conversation_history)

    # Extract AI's response
    ai_reply = response["message"]["content"]
    print(f"AI: {ai_reply}")

    # Append AI response to history
    conversation_history.append({"role": "assistant", "content": ai_reply})

    return ai_reply

# Interactive Chat Loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break
    chat_with_llama(user_input)
