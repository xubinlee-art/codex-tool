# ArXiv Translation Tool

This project provides a minimal prototype of a web service for uploading and
translating scientific papers.

## Modules
- `src/file_parser.py` — utilities for extracting text from uploaded files.
- `src/translator.py` — thin wrapper around a machine translation model.
- `web/app.py` — FastAPI application exposing a `/translate` endpoint.

## Development
Install dependencies and start the API:
```bash
pip install fastapi uvicorn pdfminer.six transformers
uvicorn web.app:app --reload
```

Run tests:
```bash
pytest
```
