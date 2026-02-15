# 🚀 Ollama GenAI Console Assistant — `ollama_console_chat.py`

A simple interactive GenAI console application built using **Python + Ollama (Local LLM)**.

This script:

- ✅ Uses a proper SYSTEM_PROMPT
- ✅ Prevents crashes on API failure
- ✅ Handles timeout safely
- ✅ Uses safe `.get()` dictionary access
- ✅ Uses lightweight `phi` model (2–3B)

---

# 🧠 What This Application Does

This application:

1. Connects to the local Ollama REST API
2. Uses the `phi` small language model
3. Applies a system role:
   > _"You are a senior Java Spring Boot developer."_
4. Accepts user questions from the console
5. Returns concise AI-generated answers
6. Runs continuously until the user types `exit`

---

# 🏗 Architecture Overview

User Input (Console)
↓
Python Script (requests)
↓
Ollama REST API (localhost:11434)
↓
phi Model (Local LLM)
↓
AI Response → Console Output

---

# ⚙️ Prerequisites

- Windows 10 / 11 (or macOS / Linux)
- Python 3.8+
- Ollama installed and running
- `requests` Python package
- `phi` model installed locally

---

# 1️⃣ Install Ollama

After installation, verify it is running:

http://localhost:11434/

You should see:

Ollama is running

---

# 2️⃣ Install the `phi` Model

Open PowerShell and run:

```powershell
ollama pull phi
Verify installation:

ollama list
Expected output:

phi
3️⃣ Setup Python Virtual Environment
Navigate to your project directory:

cd C:\path\to\your\project
Create virtual environment:

python -m venv venv
Activate it:

.\venv\Scripts\Activate.ps1
Install dependencies:

pip install --upgrade pip
pip install requests
Optional requirements.txt:

requests
Install using:

pip install -r requirements.txt
4️⃣ Run the Application
Ensure:

Ollama is running

phi model is installed

Virtual environment is activated

Run:

python ollama_console_chat.py
You will see:

Ask something (type 'exit' to quit):
Example:

Ask something (type 'exit' to quit): What is dependency injection?
Output:

AI: Dependency Injection is a design pattern where dependencies are provided externally instead of being created inside the class.
Type exit to stop the program.

🔎 Technical Breakdown
📡 API Endpoint Used
http://localhost:11434/api/generate
🤖 Model Used
phi
📝 Prompt Structure
The script combines:

SYSTEM_PROMPT
+
User Question
+
Assistant:
Example final prompt sent to the model:

You are a senior Java Spring Boot developer.
Answer clearly and concisely.

User: What is REST?
Assistant:
This improves response clarity and role alignment.

🛡 Stability & Safety Features
✅ HTTP Status Validation
response.raise_for_status()
Prevents silent HTTP failures.

✅ Safe Dictionary Access
answer = data.get("response", "No response received.")
Prevents crashes if response key is missing.

✅ Timeout Handling
timeout=180
Prevents hanging API calls.

✅ Exception Handling
except requests.exceptions.RequestException as e:
Ensures application does not crash on API failure.

🐛 Troubleshooting
❌ Connection Refused
Ensure Ollama is running

Open http://localhost:11434/

Restart Ollama service

❌ Model Not Found
ollama pull phi
❌ Slow Response
Close memory-heavy applications

Reduce:

"num_predict": 200
❌ Timeout Error
Increase timeout value:

timeout=300
📂 Suggested .gitignore
venv/
__pycache__/
*.pyc
.ollama/
.env
Thumbs.db
.DS_Store
```
