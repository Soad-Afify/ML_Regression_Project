import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.logger import LOG_FILE_PATH
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass # no need to use __init__ if we need to define variables, but we if we will create methods in the class it's better to use __inut__
class DataIngestionConfig:
    train_data_path: str= os.path.join('artifact', "train_data.csv")
    test_data_path: str= os.path.join('artifact', "test_data.csv")
    raw_data_path: str= os.path.join('artifact', "raw_data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # this attribute will sva the data in the above pathes

    def initiate_data_ingestion(self):
        '''
        This function reads the data from data source and create the path for artifact
        '''

        logging.info('Entered the data ingestion method')
        try:
            df = pd.read_csv('Notebook/data/stud.csv')
            logging.info('Data has been loaded in dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            logging.info('Train test split is intiated')
            train_set, test_set =train_test_split(df,test_size=0.2, random_state=42)

            logging.info('Save the data in artifact')
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Data ingestion is done')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)
        


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    