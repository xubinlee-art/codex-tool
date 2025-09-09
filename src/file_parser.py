"""File parsing utilities for extracting text from uploaded files."""

from typing import BinaryIO

try:
    from pdfminer.high_level import extract_text
except Exception:  # pragma: no cover - pdfminer may not be installed
    extract_text = None


def parse_uploaded_file(file_obj: BinaryIO) -> str:
    """Read a PDF or plain text file and return the extracted text.

    Parameters
    ----------
    file_obj:
        A binary file-like object pointing to the uploaded document.

    Returns
    -------
    str
        Extracted text content. If parsing fails, an empty string is
        returned.
    """
    try:
        header = file_obj.read(4)
        file_obj.seek(0)
        # very naive PDF detection
        if header.startswith(b"%PDF") and extract_text:
            # pdfminer requires a file path or file object
            return extract_text(file_obj)
        # assume utf-8 encoded text file
        return file_obj.read().decode("utf-8")
    except Exception:
        return ""
