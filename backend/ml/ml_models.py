import joblib
from catboost import CatBoostClassifier

model_1 = joblib.load('weights/decision_tree.sav')
model_2 = joblib.load('weights/logistic_weight.sav')
model_3 = CatBoostClassifier().load_model('weights/catboost')