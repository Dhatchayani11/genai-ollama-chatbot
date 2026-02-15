# Uses SYSTEM_PROMPT properly
# Prevents crash on API failure
# Handles timeout
# Cleaner formatting
# Safe .get() instead of direct dict access
# phi - small language model(2-3B)

import requests

url = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are a senior Java Spring Boot developer.
Answer clearly and concisely.
"""

while True:
    question = input("\nAsk something (type 'exit' to quit): ").strip()
    if question.lower() == "exit":
        break

    # Combine system + user prompt correctly
    full_prompt = f"{SYSTEM_PROMPT}\nUser: {question}\nAssistant:"

    try:
        response = requests.post(
            url,
            json={
                "model": "phi",
                "prompt": full_prompt,   # FIXED (was only question before)
                "stream": False,
                "options": {
                "num_predict": 200
                }
            },
            timeout=180
        )

        # Check status
        response.raise_for_status()

        data = response.json()
        answer = data.get("response", "No response received.")

        print("\nAI:", answer)

    except requests.exceptions.RequestException as e:
        print("\nError communicating with Ollama:", e)
