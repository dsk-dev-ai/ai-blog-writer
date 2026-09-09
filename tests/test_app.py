import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest

import app as app_module


@pytest.fixture
def client(monkeypatch):
    app_module.app.config.update(TESTING=True)
    return app_module.app.test_client()


def test_home_get_renders_form(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b'<form method="POST"' in resp.data


def test_home_post_empty_topic_prompts_user(client):
    resp = client.post("/", data={"topic": "   "})
    assert resp.status_code == 200
    assert "Please enter a topic" in resp.get_data(as_text=True)


def test_home_post_calls_generate_blog(client, monkeypatch):
    captured = {}

    def fake_generate(topic):
        captured["topic"] = topic
        return f"Blog about {topic}"

    monkeypatch.setattr(app_module, "generate_blog", fake_generate)
    resp = client.post("/", data={"topic": "gardening"})
    body = resp.get_data(as_text=True)
    assert captured["topic"] == "gardening"
    assert "Blog about gardening" in body


def test_generate_blog_returns_error_when_ollama_down(monkeypatch):
    monkeypatch.setattr(app_module, "OLLAMA_URL", "http://127.0.0.1:9")
    result = app_module.generate_blog("any topic")
    assert result.startswith("Error:")


def test_generate_blog_parses_ollama_response(monkeypatch):
    class FakeResp:
        def __init__(self, data):
            self._data = data

        def read(self):
            return self._data

    class FakeUrlopen:
        def __init__(self, result):
            self._result = result

        def __enter__(self):
            return self._result

        def __exit__(self, *args):
            return False

    monkeypatch.setattr(
        app_module.urllib.request,
        "urlopen",
        lambda *_a, **_k: FakeUrlopen(FakeResp(b'{"response": "hello world"}')),
    )
    assert app_module.generate_blog("test") == "hello world"