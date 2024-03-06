import pickle

import pandas as pd


def logistic_predict(X):
    """
    Initialize and load a Logistic Regression model from a file, and use it to predict the given input data.

    Parameters:
        X (array-like): The input data to be predicted.

    Returns:
        array-like: The predicted values for the input data.
    """
    logistic_model = pickle.load(open("weights/logistic_weight.sav", "rb"))
    return logistic_model.predict(X)


if __name__ == "__main__":
    df = pd.read_csv("data/interim/TUANDROMD_clear.csv")
    logistic_predict(X)
