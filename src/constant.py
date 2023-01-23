import os

VID_MIN = 115
VID_MAX = 145

OUTPUT_DIR = "/workdir/output"
RAW_MESSAGES_DIR = os.path.join(OUTPUT_DIR, "raw")
GENERATOR_TRAIN_DATA_DIR = os.path.join(OUTPUT_DIR, "generator")
FILTER_TRAIN_DATA_DIR = os.path.join(OUTPUT_DIR, "filter")

USER_ID_LIST = ["楽天家 ゲルト", "ならず者 ディーター", "パン屋 オットー", "少年 ペーター", "羊飼い カタリナ", "村長 ヴァルター", "旅人 ニコラス", "青年 ヨアヒム", "神父 ジムゾン", "少女 リーザ", "村娘 パメラ", "宿屋の女主人 レジーナ", "老人 モーリッツ", "農夫 ヤコブ", "行商人 アルビン", "木こり トーマス"]
