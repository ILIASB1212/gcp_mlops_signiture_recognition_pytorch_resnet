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