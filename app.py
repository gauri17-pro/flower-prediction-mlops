from flask import Flask, request, jsonify
import joblib
import os 
from pathlib import Path

app = Flask(__name__)
MODEL_PATH = Path("artifacts/model.pkl")

if not MODEL_PATH.exists():
    import train as _train
    _train.main()

model = joblib.load(MODEL_PATH)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "Invalid input, 'features' key missing"}), 400
    features = data["features"]
    try:
        prediction = model.predict([features])
        return jsonify({"prediction": int(prediction[0])}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)