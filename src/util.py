import os

from constant import RAW_MESSAGES_DIR


def preprocess_text(text):
    text = text.replace('"', '')
    text = text.replace("'", "")
    text = text.replace("\n", "")
    return text


def messages_path(i):
    return os.path.join(RAW_MESSAGES_DIR, "werewolf_bbs_messages_"+str(i)+".csv")
