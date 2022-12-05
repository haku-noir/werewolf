import os
import pandas as pd
from constant import VID_MAX, VID_MIN

INPUT_DATASET_DIR = "output/bbs"
OUTPUT_DATASET_DIR = "output/generator"


def preprocess_text(text):
    text = text.replace('"', '')
    text = text.replace("'", "")
    text = text.replace("\n", "")
    return text


def convert_generator_train_data(message_path, train_data_path):
    from_df = pd.read_csv(message_path, index_col=0)
    train_data = []
    prev_message = preprocess_text(from_df['message'][0])
    for message in from_df['message'][1:]:
        now_message = preprocess_text(message)
        train_data.append([prev_message, now_message])
        prev_message = now_message
    to_df = pd.DataFrame(train_data, columns=['input', 'output'])
    to_df.to_csv(train_data_path, mode='a', header=False, index=False)


if __name__ == '__main__':
    output_path = str(os.path.join(OUTPUT_DATASET_DIR, "werewolf_io_messages.csv"))
    for i in range(VID_MIN, VID_MAX+1):
        input_path = str(os.path.join(INPUT_DATASET_DIR, "werewolf_bbs_messages_"+str(i)+".csv"))
        convert_generator_train_data(input_path, output_path)
