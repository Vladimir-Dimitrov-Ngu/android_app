import joblib
from catboost import CatBoostClassifier

model_1 = joblib.load('/Users/vladimirdimitrov/My_dev/weights/decision_tree.sav')
model_2 = joblib.load('/Users/vladimirdimitrov/My_dev/weights/logistic_weight.sav')
model_3 = CatBoostClassifier().load_model('/Users/vladimirdimitrov/My_dev/weights/catboost')