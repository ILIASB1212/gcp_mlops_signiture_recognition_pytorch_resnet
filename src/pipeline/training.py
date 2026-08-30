import os
import sys
from src.components import data_transformation
from src.components.data_transformation import DataTransformation
from src.entitys.artifact import DataIngestionArtifacts,DataTransformationArtifacts
from src.loggings import logging
from src.exceptions.custom_exceptions import CustomException
from src.components.data_ingestion import DataIngestion
from src.entitys.config import DataIngestionConfig,DataTransformationConfig


class TrainingPipeline:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()

    def start_data_ingestion(self) -> DataIngestionConfig:
        logging.info("Entered the start_data_ingestion method of TrainingPipeline class")
        try:
            logging.info("Getting the dataset from GCLoud Storage bucket")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the dataset from GCLoud Storage")
            logging.info("Exited the start_data_ingestion method of TrainingPipeline class")
            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e, sys) 




    def start_data_transformation(self, data_ingestion_artifacts: DataIngestionArtifacts) -> DataTransformationArtifacts:
        logging.info("Entered the start_data_transformation method of TrainPipeline class")
        try:

            data_transformation = DataTransformation(
                data_ingestion_artifacts=data_ingestion_artifacts,
                data_transformation_config=self.data_transformation_config
            )
            data_transformation_artifacts = data_transformation.initiate_data_transformation()
            logging.info("Exited the start_data_transformation method of TrainPipeline class")

            return data_transformation_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e



    def run_pipeline(self) -> None:
        logging.info("Entered the run_pipeline method of TrainingPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_transformation_artifacts = self.start_data_transformation(
                data_ingestion_artifacts=data_ingestion_artifacts
            )
        except Exception as e:
            raise CustomException(e, sys) 

    

        




