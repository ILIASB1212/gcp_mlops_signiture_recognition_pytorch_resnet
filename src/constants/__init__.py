import os
import torch
from datetime import datetime

# Common constants
CONFIG_PATH: str = os.path.join(os.getcwd(), "config", "config.yaml")
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
Use_cuda = torch.cuda.is_available()
DEVICE = torch.device("cuda:0" if Use_cuda else "cpu")
# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = 'DataIngestionArtifacts'
DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationArtifacts"
DATA_TRANSFORMATION_TRAIN_FILE_NAME = "train_transformed.pkl"
DATA_TRANSFORMATION_VALID_FILE_NAME = "valid_transformed.pkl"
DATA_TRANSFORMATION_TEST_FILE_NAME = "test_transformed.pkl"


MODEL_TRAINER_ARTIFACTS_DIR = "ModelTrainerArtifacts"
TRAINED_MODEL_PATH = "model.pt"




MODEL_EVALUATION_ARTIFACTS_DIR = "ModelEvaluationArtifacts"
BEST_MODEL_DIR = "best_model"
MODEL_NAME = "model.pt"