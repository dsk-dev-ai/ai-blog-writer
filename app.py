from flask import Flask, render_template, request
import os
import json
import urllib.request
import urllib.error

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "phi")


def generate_blog(topic):
    prompt = f"Write a short 120-word blog about {topic}"

    payload = json.dumps({
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }).encode("utf-8")

    try:
        req = urllib.request.Request(
            OLLAMA_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("response", "")
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, json.JSONDecodeError) as e:
        return f"Error: could not generate blog — Ollama unavailable ({e})"


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        topic = request.form.get("topic", "").strip()
        if not topic:
            result = "Please enter a topic."
        else:
            result = generate_blog(topic)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")
