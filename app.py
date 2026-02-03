from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# your ollama path
OLLAMA_PATH = r"C:\Users\kacha\AppData\Local\Programs\Ollama\ollama.exe"


def generate_blog(topic):
    prompt = f"Write a short 120-word blog about {topic}"

    result = subprocess.run(
        [OLLAMA_PATH, "run", "phi", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    return result.stdout


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        topic = request.form["topic"]
        result = generate_blog(topic)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
