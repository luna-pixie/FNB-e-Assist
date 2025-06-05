import openai
import os

def get_api_key():
    api_key_path = r"C:\sheenah\api.txt"
    if not os.path.exists(api_key_path):
        print(f"❌ API key file not found at: {api_key_path}")
        return None
    with open(api_key_path, "r") as file:
        api_key = file.read().strip()
        if not api_key:
            print("❌ API key file is empty.")
            return None
        return api_key

def send_to_gpt(prompt):
    api_key = get_api_key()
    if not api_key:
        return "Failed to load API key."

    openai.api_key = api_key  # Authenticate with OpenAI

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI bank teller."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=150
        )
        return response.choices[0].message["content"].strip()
    except openai.error.AuthenticationError as auth_err:
        return f"Authentication Error: {auth_err}"
    except Exception as e:
        return f"An error occurred: {e}"
