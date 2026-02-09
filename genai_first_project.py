import requests

url = "http://localhost:11434/api/generate"


SYSTEM_PROMPT = """
You are a senior Java Spring Boot developer.
Answer clearly and concisely.
"""

while True:
    question = input("\nAsk something (type 'exit' to quit): ")
    if question.lower() == "exit":
        break

    prompt = SYSTEM_PROMPT + "\nUser: " + question + "\nAssistant:"

    response = requests.post(
        url,
        json={
            "model": "mistral",
            "prompt": question,
            "stream": False
        }
    )

    answer = response.json()["response"]
    print("\nAI:", answer)
