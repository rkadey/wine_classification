from entity.config_entity import DataIngestionConfig
from components.data_ingestion import DataIngestion
from constants import *

config = DataIngestionConfig(
    data_ingestion_dir="artifacts/data_ingestion",
    feature_store_file_path="artifacts/data_ingestion/feature_store/wine.csv",
    training_file_path="artifacts/data_ingestion/ingested/train.csv",
    testing_file_path="artifacts/data_ingestion/ingested/test.csv",
    train_test_split_ratio=0.8,
    collection_name="wine_quality"
)

ingestion = DataIngestion(config)
artifact = ingestion.ingest_data()
print(artifact)