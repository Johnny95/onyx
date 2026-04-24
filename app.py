from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

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
