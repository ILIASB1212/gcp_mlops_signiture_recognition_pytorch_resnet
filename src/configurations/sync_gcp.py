import os
import sys

from src.exceptions.custom_exceptions import CustomException






class GCloudSync:

    def sync_file_from_gcloud(self, gcp_bucket_url, filename, destination):

        #param gop_bucket_urt : GCP bucket url
        #param filepoth: filepath
        #param destinotion: where to store

        try:
            
            command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
            os.system(command)
        except Exception as e:
            raise CustomException(e, sys) from e



    def sync_file_to_gcloud(self, gcp_bucket_url, filepath):

    #parom gop_oucket_url : GCP bucket urt
    # paron filepath: filepath

        try:
            # command = f"gsutil cp {filepath} gs://{gcp_bucket_url}/"
            command = f"gcloud storage cp {filepath} gs://{gcp_bucket_url}/"
            os.system(command)
        except Exception as e:
            raise CustomException(e, sys) from e