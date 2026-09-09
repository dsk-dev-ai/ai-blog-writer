# Security

## Reporting a vulnerability

Please do **not** open a public issue for security problems. Report via a
[private security advisory](https://github.com/dsk-dev-ai/ai-blog-writer/security/advisories)
on GitHub. We aim to acknowledge reports within 3 business days.

## Dependencies

This app optionally calls a local [Ollama](https://ollama.com/) server for
text generation. By default it does not send data to third-party services.

- Never commit API keys or secrets.
- Keep dependencies current (`pip-audit` before release).