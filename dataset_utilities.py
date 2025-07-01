import os

import io


from dotenv import load_dotenv



#load environment variables
load_dotenv()

#Store relevant environment variables
KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY= os.getenv("KAGGLE_KEY")

print(f"Username: {KAGGLE_USERNAME} \n Key: {KAGGLE_KEY}")
from kaggle.api.kaggle_api_extended import KaggleApi
if not KAGGLE_USERNAME or not KAGGLE_KEY:
    raise ValueError("KAGGLE_USERNAME OR KAGGLE_KEY NOT DEFINED IN ENVIRONMENT VARIABLES")

#Create kaggle api instance
api=KaggleApi()

api._username=KAGGLE_USERNAME
api._key=KAGGLE_KEY
api.authenticate()


KAGGLE_DATASET="https://www.kaggle.com/datasets/akshaybe/updated-mimic-iv"

file_bytes= api.dataset_download_file(
    dataset=KAGGLE_DATASET
)

