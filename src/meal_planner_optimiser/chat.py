import ollama

messages = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(model="llama3.2", messages=messages)
    reply = response["message"]["content"]

    print(f"Bot: {reply}")
    messages.append({"role": "assistant", "content": reply})
