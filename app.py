# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask on Vercel working!"})

# Mock endpoint (simulate RapidAPI response)
@app.route("/api/trainstatus/<train_number>", methods=["GET"])
def train_status(train_number):
    # In production you'd call RapidAPI here using your stored key.
    # For testing we return a deterministic mock response.
    response = {
        "train_number": train_number,
        "current_station": "JTJ",
        "message": f"Train {train_number} crossed Mulanur at 11:58",
        "timestamp": "2025-11-04T12:03:30+05:30"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()
