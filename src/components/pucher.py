from src.loggings import logging
from src.exceptions.custom_exceptions import CustomException


import os
import sys
import torch
from tqdm import tqdm
from src.constants import DEVICE
from torch.utils.data import DataLoader
from src.utils.main import load_object
from src.configurations.sync_gcp import GCloudSync
from src.entitys.config import ModelEvaluationConfig
from src.entitys.artifact import ModelPusherArtifacts, ModelTrainerArtifacts, DataTransformationArtifacts,ModelEvaluationArtifacts





from src.entitys.config import ModelPusherConfig
from src.entitys.artifact import ModelTrainerArtifacts

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig,
                        model_trainer_artifacts: ModelTrainerArtifacts):


        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifacts = model_trainer_artifacts
        self.gcloud = GCloudSync()

def initiate_model_pusher(self) -> ModelPusherArtifacts:


    logging.info("Entered initiate_model_pusher method of ModelPusher class")
    try:
        logging.info("Uploading the model to gcloud storage")
        self.gcloud.sync_file_to_gcloud(self.model_pusher_config.BUCKET_NAME,
                                        self.model_trainer_artifacts.trained_model_path)
        logging.info("Uploaded best model to gcloud storage")
        logging.info("Saving the model pusher artifacts")
        model_pusher_artifact = ModelPusherArtifacts(bucket_name=self.model_pusher_config.BUCKET_NAME)
        logging.info("Exited the initiate_model_pusher method of ModelPusher class")
        return model_pusher_artifact
    except Exception as e:
        raise CustomException(e, sys) from e

        