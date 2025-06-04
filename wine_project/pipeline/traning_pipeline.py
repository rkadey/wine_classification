from wine_project.entity.config_entity import DataIngestionConfig
from wine_project.entity.artifact_entity import DataIngestionArtifact
from wine_project.components.data_ingestion import DataIngestion
from wine_project.constants import *
from wine_project.exception import WineException
from wine_project.logger import logging
import sys

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
      


    
    def start_ingest_data(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from notebooks")
            data_ingestion = DataIngestion(config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.ingest_data()
            logging.info("Got the train_set and test_set from feature store")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise WineException(e, sys) from e
        


    def run_pipeline(self) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact = self.start_ingest_data()
        
        except Exception as e:
            raise WineException(e, sys)