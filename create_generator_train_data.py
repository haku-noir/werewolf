import pandas as pd

def create_generator_train_data(from_file_path, to_file_path):
  from_df = pd.read_csv(from_file_path, index_col=0, encoding='cp932')
  train_data = []
  prev_message = from_df['message'][0]
  for message in from_df['message'][1:]:
    train_data.append([prev_message, message])
    prev_message = message
  to_df = pd.DataFrame(train_data, columns=['input', 'output'])
  to_df.to_csv(to_file_path, encoding='cp932')

if __name__ == '__main__':
  BBS_MESSAGE_PATH = "output/bbs/werewolf_bbs_messages_100.csv"
  TRAIN_DATA_PATH = "output/generator/train_data_100.csv"
  create_generator_train_data(BBS_MESSAGE_PATH, TRAIN_DATA_PATH)
