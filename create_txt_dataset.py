import os
import pandas as pd

INPUT_DATASET_DIR = "output/generator"
OUTPUT_DATASET_DIR = "output/generator"


def convert_messages_csv_to_txt_dataset(csv_path, txt_path):
    df = pd.read_csv(csv_path, header=None, names=["input", "output"])
    input_list = df["input"].tolist()
    output_list = df["output"].tolist()

    text_list = []
    for input_text, output_text in zip(input_list, output_list):
        text = "<s>" + input_text + "[SEP]" + output_text + "</s>"
        text_list.append(text)

    with open(txt_path, "a", encoding="utf8") as f:
        f.write("\n".join(text_list))


def convert_messages_csv_to_txt_dataset_including_user(csv_path, txt_path):
    df = pd.read_csv(csv_path, header=None, names=["input_user", "input", "output_user", "output"])
    input_user_list = df["input_user"].tolist()
    input_list = df["input"].tolist()
    output_user_list = df["output_user"].tolist()
    output_list = df["output"].tolist()

    text_list = []
    for input_user, input_text, output_user, output_text in zip(input_user_list, input_list, output_user_list, output_list):
        text = "<s>" + input_user + "[SEP]" + input_text + "[SEP]" + output_user + "[SEP]" + output_text + "</s>"
        text_list.append(text)

    with open(txt_path, "a", encoding="utf8") as f:
        f.write("\n".join(text_list))


if __name__ == "__main__":
    INCLUDE_USER = True

    if INCLUDE_USER:
        input_path = str(os.path.join(INPUT_DATASET_DIR, "werewolf_io_messages_including_user.csv"))
        output_path = str(os.path.join(OUTPUT_DATASET_DIR, "werewolf_messages_including_user.txt"))
        convert_messages_csv_to_txt_dataset_including_user(input_path, output_path)
    else:
        input_path = str(os.path.join(INPUT_DATASET_DIR, "werewolf_io_messages.csv"))
        output_path = str(os.path.join(OUTPUT_DATASET_DIR, "werewolf_messages.txt"))
        convert_messages_csv_to_txt_dataset(input_path, output_path)
