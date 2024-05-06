import os , sys , pickle 
from src.exception import CustomException
from src.logger import logging


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
        logging.info('Object saved successfully')
    except Exception as e:
        logging.info('Exception occured in save_object function utils')
        logging.error(str(e))
        CustomException(e,sys)