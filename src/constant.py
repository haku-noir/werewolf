import os

VID_MIN = 115
VID_MAX = 145

OUTPUT_DIR = "/workdir/output"
RAW_MESSAGES_DIR = os.path.join(OUTPUT_DIR, "raw")
GENERATOR_TRAIN_DATA_DIR = os.path.join(OUTPUT_DIR, "generator")
FILTER_TRAIN_DATA_DIR = os.path.join(OUTPUT_DIR, "filter")
