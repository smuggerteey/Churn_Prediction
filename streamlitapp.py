import pickle
import streamlit as st
import numpy as np

# Load the trained model
model = pickle.load(open(TrainedModel.pkl))

def main():
    st.title('Model Deployment with Streamlit')


    # Adding user input elements
    tenure = st.number_input('Tenure', value=1)
    monthly_charges = st.number_input('Monthly Charges', value=1.0)
    internet_service_fiber = st.checkbox('Internet Service: Fiber Optic')
    online_security = st.checkbox('Online Security: No')
    device_protection = st.checkbox('Device Protection: No Internet Service')
    tech_support = st.checkbox('Tech Support: No')
    streaming_tv = st.checkbox('Streaming TV: No Internet Service')
    streaming_movies = st.checkbox('Streaming Movies: No Internet Service')
    contract_monthly = st.checkbox('Contract: Month-to-Month')
    contract_two_year = st.checkbox('Contract: Two Year')
    payment_electronic_check = st.checkbox('Payment Method: Electronic Check')


    # Rendering the HTML file
    with open('C:/Users/Cicada 3301/Desktop/AI_Assignment3/churn_prediction.html') as f:
        html_content = f.read()
    st.markdown(html_content, unsafe_allow_html=True)

    # Process user input and make predictions

    # ...

    # Process user input and make predictions
    if st.button('Predict'):
        input_data = [
            tenure,
            monthly_charges,
            1 if internet_service_fiber else 0,
            1 if online_security else 0,
            1 if device_protection else 0,
            1 if tech_support else 0,
            1 if streaming_tv else 0,
            1 if streaming_movies else 0,
            1 if contract_monthly else 0,
            1 if contract_two_year else 0,
            1 if payment_electronic_check else 0
        ]
        input_array = np.array(input_data).reshape(1, -1)
        predictions = model.predict(input_array)
        st.write('Predicted Class:', predictions)

if __name__ == '__main__':
    main() 
