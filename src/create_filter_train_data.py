import os
import pandas as pd

from constant import FILTER_TRAIN_DATA_DIR, USER_ID_LIST, VID_MAX, VID_MIN
from util import messages_path, preprocess_text


def create_filter_train_data(from_file_path, to_file_path):
    from_df = pd.read_csv(from_file_path, index_col=0)
    train_data = []
    for name, message in zip(from_df['name'], from_df['message']):
        train_data.append([USER_ID_LIST.index(name), name, preprocess_text(message)])
    to_df = pd.DataFrame(train_data, columns=['user_id', 'name', 'message'])
    to_df.to_csv(to_file_path, mode='a', header=False, index=False)


if __name__ == '__main__':
    output_path = os.path.join(FILTER_TRAIN_DATA_DIR, "werewolf_filter_messages.csv")
    for i in range(VID_MIN, VID_MAX+1):
        create_filter_train_data(messages_path(i), output_path)
