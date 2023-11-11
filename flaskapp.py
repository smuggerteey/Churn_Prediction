import pickle
from flask import Flask, render_template, request, json, jsonify


app = Flask(__name__)

# Load the trained model
model = pickle.load(open('C:/Users/Cicada 3301/Desktop/AI_Assignment3/TrainedModel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        tenure = float(request.form['tenure'])
        monthly_charges = float(request.form['monthly_charges'])
        internet_service_fiber = int(request.form.get('internet_service_fiber', 0))
        online_security = int(request.form.get('online_security', 0))
        device_protection = int(request.form.get('device_protection', 0))
        tech_support = int(request.form.get('tech_support', 0))
        streaming_tv = int(request.form.get('streaming_tv', 0))
        streaming_movies = int(request.form.get('streaming_movies', 0))
        contract_monthly = int(request.form.get('contract_monthly', 0))
        contract_two_year = int(request.form.get('contract_two_year', 0))
        payment_electronic_check = int(request.form.get('payment_electronic_check', 0))

        input_data = [tenure, monthly_charges, internet_service_fiber, online_security, 
                      device_protection, tech_support, streaming_tv, streaming_movies, 
                      contract_monthly, contract_two_year, payment_electronic_check]

        input_array = [input_data]
        predictions = model.predict(input_array)

        return render_template('result.html', predictions=predictions[0])

if __name__ == '__main__':
    app.run(debug=True)
