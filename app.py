from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

def yes_no_to_int(value):
    return 1 if value.lower() == 'yes' else 0

def sex_to_int(value):
    return 1 if value.lower() == 'male' else 0

model = joblib.load('model.pkl')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    # Convert inputs
    age = float(request.form['age'])
    creatinine_phosphokinase = float(request.form['creatinine_phosphokinase'])
    ejection_fraction = float(request.form['ejection_fraction'])
    platelets = float(request.form['platelets'])
    serum_creatinine = float(request.form['serum_creatinine'])
    serum_sodium = float(request.form['serum_sodium'])

    anaemia = yes_no_to_int(request.form['anaemia'])
    diabetes = yes_no_to_int(request.form['diabetes'])
    high_blood_pressure = yes_no_to_int(request.form['high_blood_pressure'])
    smoking = yes_no_to_int(request.form['smoking'])

        # Convert sex to int
    sex = sex_to_int(request.form['sex'])

        # Features array for your model
    features = [
            age,
            anaemia,
            creatinine_phosphokinase,
            diabetes,
            ejection_fraction,
            high_blood_pressure,
            platelets,
            serum_creatinine,
            serum_sodium,
            smoking,
            sex        ]
    prediction = model.predict([features])[0]
    result_text = f"Predicted outcome: {prediction}"
  
    if prediction == 1:
        result_text = "Death Event"
    else:
        result_text = "No Death Event"

    # Pass the result text and prediction code if needed
    return render_template('index.html', result=result_text, prediction=prediction)
   
        
        # Replace the following with your model prediction code:
        #prediction = your_model.predict([features])
        # For demo, let's assume a dummy prediction:
   
        # Compose result string
    
   

if __name__ == "__main__":
    app.run(debug=True)
