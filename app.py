import pickle
from flask import Flask, request, jsonify, redirect
import numpy as np

# Load the trained Linear Regression model
model = pickle.load(open("linearr_rregression_model.pkl", "rb"))

# Create a Flask app
app = Flask(__name__)

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

@app.route("/")
def home():
    return redirect("/streamlit")

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')





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



