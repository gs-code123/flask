from flask import Flask, render_template, request
import joblib
import numpy as np

# Create a Flask app
app = Flask(__name__,template_folder= "templates")

# Load the pre-trained ML model
model = joblib.load('insurance_joblib')
poly_obj = joblib.load("poly_obj")

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])
        num_children = int(request.form['num_children'])
        smoking = int(request.form['smoking'])  # Assuming smoking is 0 (No) or 1 (Yes)

        # Prepare the data for the model (ensure it matches model's expected input)
        input_data = [[age, bmi, num_children, smoking]]
        poly_data = poly_obj.transform(input_data)

        # Make prediction
        prediction = np.exp(model.predict(poly_data))[0]

    return render_template('form.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
