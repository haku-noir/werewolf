import pandas as pd

def create_filter_train_data(from_file_path, to_file_path, name):
  from_df = pd.read_csv(from_file_path, index_col=0, encoding='cp932')
  to_df = from_df[from_df['name'] == name]
  to_df = to_df.reset_index()
  to_df = to_df.rename(columns={'index': 'message_id'})
  to_df.to_csv(to_file_path, encoding='cp932')

if __name__ == '__main__':
  BBS_MESSAGE_PATH = "output/bbs/werewolf_bbs_messages_100.csv"
  # TRAIN_DATA_PATH = "output/filter/train_data_gerd_100.csv"
  # NAME = "楽天家 ゲルト"
  TRAIN_DATA_PATH = "output/filter/train_data_alvin_100.csv"
  NAME = "行商人 アルビン"
  create_filter_train_data(BBS_MESSAGE_PATH, TRAIN_DATA_PATH, NAME)
