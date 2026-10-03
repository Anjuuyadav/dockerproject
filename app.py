from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return jsonify({
        "message": "Student Performance Prediction API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    required_fields = [
        "hours_studied",
        "attendance",
        "previous_score"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing field: {field}"
            }), 400

    hours = data["hours_studied"]
    attendance = data["attendance"]
    previous_score = data["previous_score"]

    if hours < 0 or attendance < 0 or attendance > 100 or previous_score < 0 or previous_score > 100:
        return jsonify({
            "error": "Invalid input values"
        }), 400

    prediction = model.predict([
        [hours, attendance, previous_score]
    ])

    return jsonify({
        "predicted_score": round(float(prediction[0]), 2)
    })


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)