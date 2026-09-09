# 🚀 AI Blog Writer (FREE Local AI)

A modern AI-powered blog generator built with Python and Flask that runs 100% locally using Ollama (no API costs).

## ✨ Features
- Generate blogs instantly
- Works offline
- FREE forever (no OpenAI charges)
- Modern UI
- Fast local LLM
- Flask backend

## 🛠 Tech Stack
- Python
- Flask
- Ollama
- HTML/CSS

## 📸 Screenshot
<img width="960" height="540" alt="1" src="https://github.com/user-attachments/assets/41cdd30e-f933-4088-aeb3-78878e61acb1" />
<img width="960" height="540" alt="2" src="https://github.com/user-attachments/assets/619fdaf1-2bd9-49d2-9007-2835c57381bf" />


## ▶️ Run Locally

```bash
pip install flask
python app.py
```
Then open:
http://127.0.0.1:5000

## 🧪 Tests

```bash
pip install -r requirements-dev.txt
python -m pytest -q
```

Tests cover the home route (GET/POST), empty-topic validation, blog
generation via the Ollama client, and Ollama-unreachable error handling.
CI runs the suite on every push.

👨‍💻 Author
Darshan Kachare
AI Developer | Automation Builder

---
