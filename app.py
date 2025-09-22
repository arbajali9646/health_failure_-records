from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load your model (if you have trained one)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    age = float(request.form['age'])
    anaemia = int(request.form['anaemia'])
    creatinine_phosphokinase = float(request.form['creatinine_phosphokinase'])
    diabetes = int(request.form['diabetes'])
    ejection_fraction = float(request.form['ejection_fraction'])
    high_blood_pressure = int(request.form['high_blood_pressure'])
    platelets = float(request.form['platelets'])
    serum_creatinine = float(request.form['serum_creatinine'])
    serum_sodium = float(request.form['serum_sodium'])
    sex = int(request.form['sex'])
    smoking = int(request.form['smoking'])

    # Prepare the feature array
    features = np.array([[age, anaemia, creatinine_phosphokinase, diabetes, 
                          ejection_fraction, high_blood_pressure, platelets, 
                          serum_creatinine, serum_sodium, sex, smoking]])

    # Make prediction using model (dummy output here)
    # prediction = model.predict(features)[0]
    prediction = 0  # Replace with model prediction

    # Display result
    result = "Patient might have high risk" if prediction == 1 else "Patient might have low risk"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
