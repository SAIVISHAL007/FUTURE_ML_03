import re

def clean_text(text):
    """
    Lowercases and removes unwanted characters.
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text
