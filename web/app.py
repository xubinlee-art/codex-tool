"""Minimal FastAPI application for translating uploaded papers."""

from fastapi import FastAPI, File, UploadFile, HTTPException

from src.file_parser import parse_uploaded_file
from src.translator import translate_text

app = FastAPI()


@app.post("/translate")
async def translate(file: UploadFile = File(...)) -> dict:
    try:
        text = parse_uploaded_file(file.file)
        translated = translate_text(text)
        return {"translated_text": translated}
    except Exception as exc:  # pragma: no cover - safety net
        raise HTTPException(status_code=500, detail=str(exc))
