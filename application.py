from flask import Flask, request, render_template
import pickle
import numpy as np

application = Flask(__name__)
app = application

# Load model and scaler
model_ridge = pickle.load(open(r'C:\Users\Radheshyam\Desktop\Algerian_Forest_fire\Model\ridge.pkl', 'rb'))
scaler = pickle.load(open(r'C:\Users\Radheshyam\Desktop\Algerian_Forest_fire\Model\scaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')  # Welcome page

@app.route("/predictdata", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
            # Get form values
            Temperature = float(request.form.get("Temperature"))
            RH = float(request.form.get("RH"))
            Ws = float(request.form.get("Ws"))
            Rain = float(request.form.get("Rain"))
            FFMC = float(request.form.get("FFMC"))
            DMC = float(request.form.get("DMC"))
            ISI = float(request.form.get("ISI"))
            Classes = float(request.form.get("Classes"))
            Region = float(request.form.get("Region"))

            # Prepare input for model
            input_data = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
            prediction = model_ridge.predict(input_data)[0]

            return render_template("home.html", prediction_text=f"{prediction:.2f}")
        except Exception as e:
            return render_template("home.html", prediction_text=f"Error: {str(e)}")
    else:
        # Always load home.html for GET requests
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
