from wine_project.entity.config_entity import DataIngestionConfig
from wine_project.components.data_ingestion import DataIngestion
from wine_project.constants import *

config = DataIngestionConfig(
    data_ingestion_dir="artifacts/data_ingestion",
    feature_store_file_path="artifacts/data_ingestion/feature_store/wine.csv",
    training_file_path="artifacts/data_ingestion/ingested/train.csv",
    testing_file_path="artifacts/data_ingestion/ingested/test.csv",
    train_test_split_ratio=0.8,
)

ingestion = DataIngestion(config)
artifact = ingestion.ingest_data()