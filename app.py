# -*- coding: utf-8 -*-
"""
Created on Thr Sep 23 15:14:04 2021

@author: VISHAL UPARE
"""
# %%

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

# %%

app = Flask(__name__)

# %%

model = pickle.load(open("model_EXT.pkl", "rb"))

# %%


@app.route("/")
def home():
    return render_template("home.html")

# %%


@app.route("/PID", methods=['POST'])
def PID():

    data = request.form["names"]
    data1 = request.form["Pregnancies"]
    data2 = request.form["Glucose"]
    data3 = request.form["BloodPressure"]
    data4 = request.form["SkinThickness"]
    data5 = request.form["Insulin"]
    data6 = request.form["BMI"]
    data7 = request.form["DiabetesPedigreeFunction"]
    data8 = request.form["Age"]

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    prediction = model.predict(arr)

    # create original output dict
    output_dict1 = dict()
    output_dict1['Name'] = data
    output_dict1['Pregnancies'] = data1
    output_dict1['Glucose'] = data2
    output_dict1['BloodPressure'] = data3
    output_dict1['SkinThickness'] = data4
    output_dict1['Insulin'] = data5
    output_dict1['BMI'] = data6
    output_dict1['DiabetesPedigreeFunction'] = data7
    output_dict1['Age'] = data8
    
    return render_template("result.html", original_input1=output_dict1, data=prediction)
# %%


if __name__ == '__main__':
    app.run(debug=True)

# %%
