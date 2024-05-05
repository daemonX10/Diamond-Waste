from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding for Categorical Variables convert them into Numerical Variables
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import os , sys
from dataclasses import dataclass
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging

## Data Transformation Config   

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')
    
## Data Transformation Class

class DataTransforation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_tranformation_object(self):
        try:
            logging.info('Data Transformation initiated')
            
            # Define which columns should be ordinal-encoded and which should be scaled
            
            categorical_cols = ['cut','color','clarity']
            numerical_cols = ['carat','depth','table','x','y','z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair','Good','Very Good','Premium','Ideal']
            color_categories = ['D','E','F','G','H','I','J']
            clarity_categories= ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info('Pipeline Initiated')
            
            ## Numerical Pipeline
            num_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )
            
            # Categorical Pipeline
            cat_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories]))
                ]
            )
            
            preprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols)
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            logging.info("Pipe completed")
            return preprocessor
        
        except Exception as e:
            logging.error('Error occured while Data Transformation')
            logging.error(str(e))
            raise CustomException('Error occured while Data Transformation')
        