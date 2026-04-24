from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

latest_image = None
chosen_card = None

@app.route('/')
def home():
    return "Server running"

@app.route('/upload', methods=['POST'])
def upload():
    global latest_image
    latest_image = request.json['image']
    return 'ok'

@app.route('/set_card', methods=['POST'])
def set_card():
    global chosen_card
    chosen_card = request.json['card']
    return 'ok'

@app.route('/result')
def result():
    if latest_image and chosen_card:
        return jsonify({
            "image": latest_image,
            "card": chosen_card
        })
    return jsonify({"status": "waiting"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
