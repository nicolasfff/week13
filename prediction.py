import joblib
import numpy as np

model = joblib.load("knn_diabetes_model.sav")

def predict(data):
    arr = np.array(data).reshape(1, -1)
    return model.predict(arr)
