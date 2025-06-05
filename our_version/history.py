import os

def save_to_history(question, response, filename="chat_history.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"User: {question}\n")
        file.write(f"GPT: {response}\n")
        file.write("-" * 50 + "\n")

def read_history(filename="chat_history.txt"):
    if not os.path.exists(filename):
        return "No history available."
    
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
