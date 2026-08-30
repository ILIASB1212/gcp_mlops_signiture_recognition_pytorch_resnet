from dataclasses import dataclass
from src.utils.main import read_yaml_file
from src.constants import *




@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.config = read_yaml_file(CONFIG_PATH)
        self.BUCKET_NAME: str = self.config['data_ingestion_config']["bucket_name"]
        self.ZIP_FILE_NAME: str = self.config['data_ingestion_config']["zip_file_name"]
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, self.ZIP_FILE_NAME)





class DataTransformationConfig:


    def __Init__ (self):
        self.config = read_yaml_file(CONFIG_PATH)
        self.STD: list = self.config['data_transformation_config']["std"]
        self.MEAN: list = self.config['data_transformation_config']["mean"]
        self.IMG_SIZE: int = self.config['data_transformation_config']["img_size"]
        self.DEGREE_N: int = self.config['data_transformation_config']["degree_n"]
        self.DEGREE_P: int = self.config['data_transformation_config']["degree_p"]
        self.TRAIN_RATIO: float = self.config['data_transformation_config']["train_ratio"]
        self.VALID_RATIO: float = self.config['data_transformation_config']["valid_ratio"]
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR,
        DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRAIN_TRANSFORM_OBJECT_FILE_PATH: str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,
        DATA_TRANSFORMATION_TRAIN_FILE_NAME)
        self.VALID_TRANSFORM_OBJECT_FILE_PATH: str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,
        DATA_TRANSFORMATION_VALID_FILE_NAME)
        self.TEST_TRANSFORM_OBJECT_FILE_PATH: str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,
        DATA_TRANSFORMATION_TEST_FILE_NAME)