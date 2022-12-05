import os
import pandas as pd

from constant import FILTER_TRAIN_DATA_DIR, VID_MAX, VID_MIN
from util import messages_path


def create_filter_train_data(from_file_path, to_file_path, name):
    from_df = pd.read_csv(from_file_path, index_col=0)
    to_df = from_df[from_df['name'] == name]
    to_df = to_df.reset_index()
    to_df = to_df.rename(columns={'index': 'message_id'})
    to_df.to_csv(to_file_path)


if __name__ == '__main__':
    output_path = os.path.join(FILTER_TRAIN_DATA_DIR, "werewolf_filter_messages.csv")
    for i in range(VID_MIN, VID_MAX+1):
        create_filter_train_data(messages_path(i), output_path)
