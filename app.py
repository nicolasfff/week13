import streamlit as st
import numpy as np
from prediction import predict

st.title("Diabetes Prediction App (KNN)")

st.write("Masukkan nilai indikator kesehatan sesuai dataset:")

cols = [
    'HighBP','HighChol','CholCheck','BMI','Smoker','Stroke',
    'HeartDiseaseorAttack','PhysActivity','Fruits','Veggies','HvyAlcoholConsump',
    'AnyHealthcare','NoDocbcCost','GenHlth','MentHlth','PhysHlth','DiffWalk',
    'Sex','Age','Education','Income'
]

inputs = []

for col in cols:
    val = st.number_input(col, min_value=0.0)
    inputs.append(val)

if st.button("Predict"):
    result = predict(inputs)
    if result[0] == 0:
        st.success("Tidak Diabetes")
    elif result[0] == 1:
        st.warning("Pre-diabetes")
    else:
        st.error("Diabetes")
