import os
import sys
import torch
from src.loggings import logging
from src.exceptions.custom_exceptions import CustomException
from torchvision import datasets
from torchvision import transforms as T
from src.utils.main  import save_model
from src.entitys.config import DataTransformationConfig
from src.entitys.artifact import DataIngestionArtifacts, DataTransformationArtifacts



class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig,
        data_ingestion_artifacts: DataIngestionArtifacts):
        try:
            

            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifacts = data_ingestion_artifacts
            self.std = self.data_transformation_config.STD
            self.mean = self.data_transformation_config.MEAN
            self.img_size = self.data_transformation_config.IMG_SIZE
            self.degree_n = self.data_transformation_config.DEGREE_N
            self.degree_p = self.data_transformation_config.DEGREE_P
            self.train_ratio = self.data_transformation_config.TRAIN_RATIO
            self.valid_ratio = self.data_transformation_config.VALID_RATIC


        except Exception as e:
            raise CustomException(e, sys) from e



        try:
            logging.info("Entered the get_transform_data method of Data transformation class")
            data_transform = T.Compose([
            T.Resize(size=(self.img_size, self.img_size)), 
            T.RandomRotation(degrees=(self.degree_n, self.degree_p)),
            T.ToTensor(),
            T.Normalize(self.mean, self.std)])

            logging.info("Exited the get_transform_data method of Data transformation class")
            return data_transform

        except Exception as e:
            raise CustomException(e,sys) from e


    def split_data(self, dataset, total_count):


        try:
            logging.info("Entered the split_data method of Data transformation class")
            train_count = int(self.train_ratio * total_count)
            valid_count = int(self.valid_ratio * total_count)
            test_count = total_count - train_count - valid_count
            train_data, valid_data, test_data = torch.utils.data.random_split(dataset,
            (train_count,
            valid_count,
            test_count))
            logging.info("Exited the split_data method of Data transformation class")
            return train_data, valid_data, test_data
        except Exception as e:
            raise CustomException(e, sys) from e


    def initiate_data_transformation(self) -> DataTransformationArtifacts:

        try:
            logging.info("Entered the initiate_data_transformation method of Data transformation class")

            dataset = datasets.ImageFolder(self.data_ingestion_artifacts.dataset_path,
            transform=self.get_transform_data())

            logging.info(f"Total number of records: {total_count}")

            classes = len(os.Listdir(self.data_ingestion_artifacts.dataset_path))
            logging.info(f"Total number of classes: {classes}")

            train_dataset, valid_dataset, test_dataset = self.split_data(dataset, total_count)
            logging.info("Split dataset into train, valid and test")

            
            total_count = len(dataset)
            logging.info(f"total number of records: {total_count}")

            logging.info("Split dataset into train, valid and test")

            save_model(self.data_transformation_config.TRAIN_TRANSFORM_OBJECT_FILE_PATH, train_dataset)
            save_model(self.data_transformation_config.VALID_TRANSFORM_OBJECT_FILE_PATH, valid_dataset)
            save_model(self.data_transformation_config.TEST_TRANSFORM_OBJECT_FILE_PATH, test_dataset)

            data_transformation_artifact = DataTransformationArtifacts(
            train_transformed_object=self.data_transformation_config. TRAIN_TRANSFORM_OBJECT_FILE_PATH,
            valid_transformed_object=self.data_transformation_config.VALID_TRANSFORM_OBJECT_FILE_PATH,
            test_transformed_object=self.data_transformation_config.TEST_TRANSFORM_OBJECT_FILE_PATH,
            classes=classes)

            logging.info(f"Data transformation artifact: {data_transformation_artifact}")
            logging.info("Exited the initiate_data_transformation method of Data transformation class")
            logging.info(f"Data transformation artifact: {data_transformation_artifact}")
            logging.info("Exited the initiate_data_transformation method of Data transformation class")
            return data_transformation_artifact

        except Exception as e:
            raise CustomException(e, sys) from e