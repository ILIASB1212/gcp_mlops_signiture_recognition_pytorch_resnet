import os
import sys
from zipfile import ZipFile
from src.loggings import logging
from src.exceptions.custom_exceptions import CustomException
from src.configurations.sync_gcp import GCloudSync
from src.entitys.config import DataIngestionConfig
from src.entitys.artifact import DataIngestionArtifacts


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.gcp=GCloudSync()


    def get_data_from_gcloud(self) -> None:


        try:
            logging.info("Entered the get_data_from_gcloud method of Data ingestion class")

            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)

            self.gcp.sync_file_from_gcloud(self.data_ingestion_config.BUCKET_NAME,
            self.data_ingestion_config.ZIP_FILE_NAME,
            self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,)

            logging.info("Exited the get_data_from_gcloud method of Data ingestion class")

        except Exception as e:
            raise CustomException(e, sys) from None
    def unzip_and_clean(self) -> None:

        logging.info("Entered the unzip_and_clean method of Data ingestion class")
        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, 'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)
            logging.info("Exited the unzip_and_clean method of Data ingestion class")
        except Exception as e:
            raise CustomException(e, sys) from e


    def initiate_data_ingestion(self) -> DataIngestionArtifacts:



        logging.info("Entered the initiate_data_ingestion method of Data ingestion class")
        try:
            self.get_data_from_gcloua()
            logging.info("Fetched the zipped dataset from Gcloud Storage bucket")

            self.unzip_and_clean()
            logging.info("Unzipped the file fetched from Gcloud Storage bucket")

            logging.info("Deleting dataset.zip file*")
            os.remove(os.path.join(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,
            self.data_ingestion_config.ZIP_FILE_NAME))

            data_ingestion_artifacts = DataIngestionArtifacts(
            dataset_path=self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)

            logging.info(f"Data ingestion artifact: {data_ingestion_artifacts}*")

            logging.info("Exited the initiate_data_ingestion method of Data ingestion class")
            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e




