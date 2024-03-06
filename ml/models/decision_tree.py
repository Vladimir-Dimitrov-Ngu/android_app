import os
import pickle

import pandas as pd


def predict(model, X):
    """
    Initialize and load a Decision Tree classifier model from a file, and use it to predict the given input data.

    Parameters:
        X (array-like): The input data to be predicted.

    Returns:
        array-like: The predicted values for the input data.
    """
    return model.predict(X)
