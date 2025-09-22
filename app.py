from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = [float(x) for x in request.form.values()]
        final_input = np.array(data).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(final_input)[0]
        
        if prediction == 1:
            result = "The patient is likely to have DEATH_EVENT."
        else:
            result = "The patient is unlikely to have DEATH_EVENT."
        
        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
