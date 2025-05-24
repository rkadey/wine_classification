import os
from datetime import date

PIPELINE_NAME: str = "wineproject"
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "quality_label"
CURRENT_YEAR = date.today().year

MODEL_FILE_NAME = "wine_quality_classification.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
