import pickle
from flask import Flask, request, jsonify, redirect
import pandas as pd
import numpy as np
import streamlit as st
import requests

# Load the trained Linear Regression model
model = pickle.load(open("linearr_rregression_model.pkl", "rb"))

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/predict', methods=['POST'])
def predict():
    # Extracting data from the form
    float_features = [float(x) for x in request.form.values()]

    # Make predictions using the loaded model
    features1 = [np.array(float_features)]
    prediction = model.predict(features1)
    python_list = prediction.tolist()
    prediction1 = f'The Mental Fitness is {python_list[0]:.2f}'

    return jsonify({'message': prediction1}), 200


@app.route("/streamlit")
def streamlit():
    return redirect("http://localhost:8501/")


@app.route("/")
def home():
    return redirect("/streamlit")


# Title
st.title("Mental Fitness Prediction")
st.markdown('<div class="container">', unsafe_allow_html=True)

# Input fields
schizophrenia = st.text_input("Schizophrenia")
bipolar_disorder = st.text_input("Bipolar Disorder")
eating_disorder = st.text_input("Eating Disorder")
anxiety = st.text_input("Anxiety")
drug_usage = st.text_input("Drug Usage")
depression = st.text_input("Depression")
alcohol = st.text_input("Alcohol")

if st.button("Predict", key="predict-button"):
    # Prepare data for prediction
    data = {
        'schizophrenia': schizophrenia,
        'bipolar_disorder': bipolar_disorder,
        'eating_disorder': eating_disorder,
        'anxiety': anxiety,
        'drug_usage': drug_usage,
        'depression': depression,
        'alcohol': alcohol
    }

    # Send POST request to Flask API
    response = requests.post("http://127.0.0.1:5000/predict", data=data)

    # Display prediction result
    if response.status_code == 200:
        result = response.json()
        st.markdown(f'<div class="result">{result["message"]}</div>', unsafe_allow_html=True)
    else:
        st.error(f"Error: {response.text}")

st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)







# import pickle
# from flask import Flask, render_template, request, jsonify, redirect
# import pandas as pd
# import numpy as np


# # app = Flask(__name__)

# # # Load the trained Linear Regression model
# # with open('linearr_rregression_model.pkl', 'rb') as model_file:
# #     lr_model = pickle.load(model_file)
# app = Flask(__name__,static_folder='static',static_url_path='/static')
# model = pickle.load(open("linearr_rregression_model.pkl", "rb"))
# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Extracting data from the form
#     #   if request.form:
#     #     # Handle form data
#     float_features = [float(x) for x in request.form.values()]
#     # features = ['Schizophrenia', 'Bipolar_disorder', 'Eating_disorder', 'Anxiety', 'drug_usage', 'depression', 'alcohol']
#     # input_data = [request.form[feature] for feature in features]
#     # float_features = [(x) for x in request.form.values()]
#     # Create a DataFrame from the input data
#     # input_df = pd.DataFrame([input_data], columns=features)

#     # Make predictions using the loaded model
#     features1 = [np.array(float_features)]
#     prediction = model.predict(features1)
#     python_list = prediction.tolist()
#     prediction1 = f'The Mental Fitness is {python_list[0]:.2f}'

#     return jsonify({'message': prediction1}), 200

#     #return render_template('index.html', prediction=prediction)

# @app.route("/streamlit")
# def streamlit():
#     return redirect("http://localhost:8501/")


# if __name__ == '__main__':
#     app.run(debug=True, host= '0.0.0.0', port=5000)



