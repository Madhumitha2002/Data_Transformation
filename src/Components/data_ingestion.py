import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class data_ingestion_config:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')

class data_ingestion:
    def __init__(self):
        self.ingestion_config = data_ingestion_config()

    def initiate_data_ingestion(self):
        logging.info("The data ingestion has been initiated")
        try:
            df= pd.read_csv('Notebook\data\fifa21_raw_data.csv')
            logging.info('The dataset has been read as dataframe')


            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok= True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, Header=True)


            logging.info('The test-train split is initiated')
            train_set, test_set = train_test_split(df, test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, Header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, Header=True)
            logging.info('Ingestion is done')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)


