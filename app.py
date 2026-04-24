from flask import Flask, request, jsonify

app = Flask(__name__)

latest_image = None
chosen_card = None


# ✅ FORCE CORS HEADERS (this is the key fix)
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response


# ✅ Handle preflight requests explicitly
@app.route('/set_card', methods=['POST', 'OPTIONS'])
def set_card():
    global chosen_card
    if request.method == 'OPTIONS':
        return '', 200
    chosen_card = request.json['card']
    return 'ok'


@app.route('/upload', methods=['POST', 'OPTIONS'])
def upload():
    global latest_image
    if request.method == 'OPTIONS':
        return '', 200
    latest_image = request.json['image']
    return 'ok'


@app.route('/result', methods=['GET'])
def result():
    if latest_image and chosen_card:
        return jsonify({
            "image": latest_image,
            "card": chosen_card
        })
    return jsonify({"status": "waiting"})


@app.route('/')
def home():
    return "Server running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
