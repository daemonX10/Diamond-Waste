import os , sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score
import numpy as np

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        
        for i in range(len(models)):
            model = list(models.values())[i] ## select model value of ith key(model)
            model.fit(X_train,y_train)
            y_test_pred = model.predict(X_test)
            ## Get R2 scores for train and test data
            test_model_score = r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]] = test_model_score

        logging.info('Model Evaluation Completed')
        return report
    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)