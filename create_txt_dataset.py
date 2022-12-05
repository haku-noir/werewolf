import os
import pandas as pd

INPUT_DATASET_DIR = "output/generator"
OUTPUT_DATASET_DIR = "output/generator"


def convert_messages_csv_to_txt_dataset(csv_path: str, txt_path: str) -> None:
    df = pd.read_csv(csv_path, header=None, names=["input", "output"])
    input_list = df["input"].tolist()
    output_list = df["output"].tolist()

    text_list = []
    for input_text, output_text in zip(input_list, output_list):
        text = "<s>" + input_text + "[SEP]" + output_text + "</s>"
        text_list.append(text)

    with open(txt_path, "a", encoding="utf8") as f:
        f.write("\n".join(text_list))


if __name__ == "__main__":
    input_path = str(os.path.join(INPUT_DATASET_DIR, "werewolf_io_messages.csv"))
    output_path = str(os.path.join(OUTPUT_DATASET_DIR, "werewolf_messages.txt"))
    convert_messages_csv_to_txt_dataset(input_path, output_path)
