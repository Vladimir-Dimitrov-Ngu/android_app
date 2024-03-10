from fastapi import HTTPException, UploadFile, File
import pandas as pd
from sklearn.metrics import accuracy_score
from backend.ml import model_1, model_2, model_3
import time
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

def predict_task(model_name: str, file: str):
    try:
        df = pd.read_csv(file, index_col=0)
        Y = df["Label"]
        X = df.drop("Label", axis=1)
        if model_name == "dt":
            predict = model_1.predict(X)
        elif model_name == "lr":
            predict = model_2.predict(X)
        else:
            predict = model_3.predict(X)
        accuracy = accuracy_score(Y, predict)
        logging.info(f"Prediction successful. Accuracy: {accuracy}")
        return {"accuracy": accuracy}
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="Empty CSV file")
    except pd.errors.ParserError:
        raise HTTPException(status_code=400, detail="Invalid CSV file format")

def my_task(x, y):
    time.sleep(1)
    return 0