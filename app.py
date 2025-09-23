from flask import Flask, request, render_template

app = Flask(__name__)

def yes_no_to_int(value):
    return 1 if value.lower() == 'yes' else 0

def sex_to_int(value):
    return 1 if value.lower() == 'male' else 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert inputs
        age = float(request.form['age'])
        creatinine_phosphokinase = float(request.form['creatinine_phosphokinase'])
        ejection_fraction = float(request.form['ejection_fraction'])
        platelets = float(request.form['platelets'])
        serum_creatinine = float(request.form['serum_creatinine'])
        serum_sodium = float(request.form['serum_sodium'])

        # Convert Yes/No to 1/0
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
            sex
        ]

        # Replace the following with your model prediction code:
        # prediction = your_model.predict([features])
        # For demo, let's assume a dummy prediction:
        prediction = "SURVIVE"  # or "HIGH RISK"

        # Compose result string
        result_text = f"Predicted outcome: {prediction}"

        return render_template('index.html', result=result_text)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
