import os
import pandas as pd

from constant import GENERATOR_TRAIN_DATA_DIR, VID_MAX, VID_MIN
from util import messages_path, preprocess_text


def create_generator_train_data(message_path, train_data_path):
    from_df = pd.read_csv(message_path, index_col=0)
    train_data = []
    prev_message = preprocess_text(from_df['message'][0])
    for message in from_df['message'][1:]:
        now_message = preprocess_text(message)
        train_data.append([prev_message, now_message])
        prev_message = now_message
    to_df = pd.DataFrame(train_data, columns=['input', 'output'])
    to_df.to_csv(train_data_path, mode='a', header=False, index=False)


def create_generator_train_data_including_user(message_path, train_data_path):
    from_df = pd.read_csv(message_path, index_col=0)
    train_data = []
    prev_user = from_df['name'][0]
    prev_message = preprocess_text(from_df['message'][0])
    for name, message in zip(from_df['name'][1:], from_df['message'][1:]):
        now_user = name
        now_message = preprocess_text(message)
        train_data.append([prev_user, prev_message, now_user, now_message])
        prev_user = now_user
        prev_message = now_message
    to_df = pd.DataFrame(train_data, columns=['input_user', 'input', 'output', 'output_user'])
    to_df.to_csv(train_data_path, mode='a', header=False, index=False)


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


if __name__ == '__main__':
    INCLUDE_USER = True

    creator = create_generator_train_data
    converter = convert_messages_csv_to_txt_dataset
    output_path = os.path.join(GENERATOR_TRAIN_DATA_DIR, "werewolf_io_messages.csv")
    output_convert_path = os.path.join(GENERATOR_TRAIN_DATA_DIR, "werewolf_io_messages.txt")

    if INCLUDE_USER:
        creator = create_generator_train_data_including_user
        converter = convert_messages_csv_to_txt_dataset_including_user
        output_path = os.path.join(GENERATOR_TRAIN_DATA_DIR, "werewolf_io_messages_including_user.csv")
        output_convert_path = os.path.join(GENERATOR_TRAIN_DATA_DIR, "werewolf_io_messages_including_user.txt")
        
    for i in range(VID_MIN, VID_MAX+1):
        creator(messages_path(i), output_path)
    converter(output_path, output_convert_path)
