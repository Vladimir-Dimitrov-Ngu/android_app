import pandas as pd
from catboost import CatBoostClassifier


def catboost_predict(X):
    """
    Initialize and load a CatBoost classifier model from a file, and use it to predict the given input data.

    Parameters:
        X (array-like): The input data to be predicted.

    Returns:
        array-like: The predicted values for the input data.
    """
    catboost_model = CatBoostClassifier()
    catboost_model.load_model("model")
    return catboost_model.predict(X)


if __name__ == "__main__":
    NUMBER_FEATURES = 10
    df = pd.read_csv("data/interim/TUANDROMD_clear.csv")
    X = df.iloc[:, :NUMBER_FEATURES]
    catboost_predict(X)
