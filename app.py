from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("weather_model_1.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        temp = float(request.form["temp"])
        humidity = float(request.form["humidity"])
        wind = float(request.form["wind"])
        pressure = float(request.form["pressure"])

        # Prepare input
        input_data = np.array([[temp, humidity, wind, pressure]])
        prediction = model.predict(input_data)[0]

        # Simple logic for weather icon
        if prediction > 30:
            weather_icon = "sunny.png"
            weather_text = "Sunny"
        elif prediction > 20:
            weather_icon = "cloudy.jpeg"
            weather_text = "Cloudy"
        else:
            weather_icon = "rainy.jpg"
            weather_text = "Rainy"

        return render_template(
            "result.html",
            prediction=round(prediction, 2),
            weather_icon=weather_icon,
            weather_text=weather_text,
            temp=temp, humidity=humidity, wind=wind, pressure=pressure
        )
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
