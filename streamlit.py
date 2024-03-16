import os
import streamlit as st
import requests

# Get the URL of the Flask app from environment variables
FLASK_URL = os.environ.get("http://localhost:5000")

# Title
st.title("Mental Fitness Prediction")
st.markdown('<div class="container">', unsafe_allow_html=True)

# Input fields
schizophrenia = st.text_input("How much do you feel overwhelmed by your work?                                (out of 100)")
bipolar_disorder = st.text_input("How much do you feel depressed or sad about your work?                (out of 100) ")
eating_disorder = st.text_input("How much do you feel that your team or Manager does not support your work?        (out of 100)  ")
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
    response = requests.post(FLASK_URL + "/predict", data=data)

    # Display prediction result
    if response.status_code == 200:
        result = response.json()
        st.markdown(f'<div class="result">{result["message"]}</div>', unsafe_allow_html=True)
    else:
        st.error(f"Error: {response.text}")

st.markdown('</div>', unsafe_allow_html=True)




# import streamlit as st
# import requests

# # Title
# st.title("Mental Fitness Prediction")
# st.markdown('<div class="container">', unsafe_allow_html=True)

# #days_left = st.text_input("Days Left", value="")

# schizophrenia = st.text_input("schizophrenia", value="")
# bipolar_disorder = st.text_input("bipolar_disorder", value="")
# eating_disorder = st.text_input("eating_disorder", value="")
# anxiety = st.text_input("anxiety", value="")
# drug_usage = st.text_input("drug_usage", value="")
# depression = st.text_input("depression", value="")
# alcohol = st.text_input("alcohol", value="")



# if st.button("Predict", key="predict-button"):
#     # Prepare data for prediction
#     data = {
        
#         'schizophrenia': schizophrenia,
#         'bipolar_disorder': bipolar_disorder,
#         'eating_disorder': eating_disorder,
#         'anxiety': anxiety,
#         'drug_usage': drug_usage,
#         'depression': depression,
#         'alcohol': alcohol

#     }

# # Send POST request to Flask API
#     response = requests.post("http://127.0.0.1:5000/predict", data=data)

#     # Display prediction result
#     if response.status_code == 200:
#         result = response.json()
#         st.markdown(f'<div class="result">{result["message"]}</div>', unsafe_allow_html=True)
#     else:
#         st.error(f"Error: {response.text}")

# st.markdown('</div>', unsafe_allow_html=True)

# # Input form
# # with st.form(key='prediction_form'):
# #     # Input fields
# #     st.subheader("Input Data")
# #     schizophrenia = st.number_input("Schizophrenia")
# #     bipolar_disorder = st.number_input("Bipolar Disorder")
# #     eating_disorder = st.number_input("Eating Disorder")
# #     anxiety = st.number_input("Anxiety")
# #     drug_usage = st.number_input("Drug Usage")
# #     depression = st.number_input("Depression")
# #     alcohol = st.number_input("Alcohol")

# #     # Submit button
# #     submitted = st.form_submit_button("Predict")

# # Prediction logic
# # if submitted:
# #     # Perform prediction here
# #     prediction = "Placeholder prediction"  # Replace with actual prediction logic
    
# #     # Display prediction result
# #     st.subheader("Prediction Result")
# #     st.write(f"Mental Fitness Prediction: {prediction}")

