def preprocess_text(text):
    text = text.replace('"', '')
    text = text.replace("'", "")
    text = text.replace("\n", "")
    return text
