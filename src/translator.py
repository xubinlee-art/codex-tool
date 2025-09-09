"""Translation utilities using a machine translation model or API."""

from typing import List

try:
    from transformers import pipeline  # type: ignore
except Exception:  # pragma: no cover - transformers may not be installed
    pipeline = None

_DEFAULT_MODEL = "Helsinki-NLP/opus-mt-en-zh"


def _chunk_text(text: str, chunk_size: int = 4000) -> List[str]:
    """Split text into manageable chunks for translation."""
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


def translate_text(text: str, target_lang: str = "zh") -> str:
    """Translate English text to another language.

    Parameters
    ----------
    text:
        Source text to translate.
    target_lang:
        Target language code. Currently only Chinese ("zh") is tested.
    """
    if not text:
        return ""

    if pipeline is None:
        # Fallback: return the original text when transformers is missing.
        return text

    translator = pipeline("translation", model=_DEFAULT_MODEL)
    chunks = _chunk_text(text)
    outputs = translator(chunks)
    return "".join(o["translation_text"] for o in outputs)
