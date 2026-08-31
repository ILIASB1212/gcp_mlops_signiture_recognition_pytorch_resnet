import os
import sys
from src.components import model_evaluation
from src.components.data_transformation import DataTransformation
from src.components.model_evaluation import ModelEvaluation
from src.entitys.config import ModelEvaluationConfig, ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
from src.entitys.artifact import DataIngestionArtifacts,DataTransformationArtifacts, ModelEvaluationArtifacts, ModelEvaluationArtifacts, ModelTrainerArtifacts
from src.loggings import logging
from src.exceptions.custom_exceptions import CustomException
from src.components.data_ingestion import DataIngestion
from src.entitys.config import DataIngestionConfig,DataTransformationConfig,modelTrainerConfig,ModelEvaluationConfig


class TrainingPipeline:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        self.model_evaluation_config = ModelEvaluationConfig()

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



    def start_model_trainer(self, data_transformation_artifacts: DataTransformationArtifacts) -> ModelTrainerArtifacts:
        logging.info("Entered the start_model_trainer method of TrainPipeline class")
        try:
            model_trainer = ModelTrainer(
            data_transformation_artifacts=data_transformation_artifacts,
            modet_trainer_config=self.model_trainer_config)

            model_trainer_artifacts = model_trainer.initiate_model_trainer()
            logging.info("Exited the start_model_trainer method of TrainPipeline class")

            return model_trainer_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e


    def start_model_evaluat (self, model_trainer_artifacts: ModelTrainerArtifacts,
        data_transformation_artifacts: DataTransformationArtifacts) -> ModelEvaluationArtifacts:

        logging.info("Entered the start_model_evaluation method of TrainPipeline class")
        try:
            model_evaluation = ModelEvaluation(
            model_evaluation_config=self.model_evaluation_config,
            data_transformation_artifacts=data_transformation_artifacts,
            model_trainer_artifacts=model_trainer_artifacts)

            model_evaluation_artifacts = model_evaluation.initiate_model_evaluation()
            logging.info("Exited the start_model_evaluation method of TrainPipeline class")
            return model_evaluation_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e





    def run_pipeline(self) -> None:
        logging.info("Entered the run_pipeline method of TrainingPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_transformation_artifacts = self.start_data_transformation(data_ingestion_artifacts=data_ingestion_artifacts)
            model_trainer_artifacts = self.start_model_trainer(data_transformation_artifacts=data_transformation_artifacts)
            model_evaluation_artifacts = self.start_model_evaluation(
                model_trainer_artifacts=model_trainer_artifacts,
                data_transformation_artifacts=data_transformation_artifacts
            )

        except Exception as e:
            raise CustomException(e, sys) 

    

        




