import os


from kaggle.api.kaggle_api_extended import KaggleApi

from dotenv import load_dotenv

load_dotenv()

KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY= os.getenv("KAGGLE_KEY")

print(f"Username: {KAGGLE_USERNAME} \n Key: {KAGGLE_KEY}")
