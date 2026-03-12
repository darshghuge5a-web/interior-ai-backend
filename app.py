from flask import Flask, request, jsonify
from flask_cors import CORS

from room_detector import detect_room
from generator import generate_room
from furniture_catalog import suggest_furniture

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "AI Interior Backend Running"


@app.route("/detect-room", methods=["POST"])
def detect():

    if "image" not in request.files:
        return jsonify({"error": "No image"}), 400

    image = request.files["image"]

    room = detect_room(image)

    return jsonify({
        "detected_room": room
    })


@app.route("/generate", methods=["POST"])
def generate():

    if "image" not in request.files:
        return jsonify({"error": "No image"}), 400

    image = request.files["image"]

    room = request.form.get("room")
    style = request.form.get("style")
    furniture = request.form.get("furniture")

    result = generate_room(image, room, style, furniture)

    return jsonify(result)


@app.route("/furniture-suggestions", methods=["POST"])
def furniture():

    room = request.json.get("room")

    suggestions = suggest_furniture(room)

    return jsonify({
        "suggestions": suggestions
    })


if __name__ == "__main__":
    app.run()
