import base64
import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

from room_detector import detect_room
from image_utils import resize_image

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


@app.route("/")
def home():
    return "AI Interior Backend Running"


@app.route("/detect-room", methods=["POST"])
def detect():

    if "image" not in request.files:
        return jsonify({"error": "No image"}), 400

    image = request.files["image"]

    room = detect_room(image)

    return jsonify({"room": room})


@app.route("/generate", methods=["POST"])
def generate():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]

    room = request.form.get("room", "")
    style = request.form.get("style", "")
    furniture = request.form.get("furniture", "")

    image_bytes = resize_image(image)

    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    prompt = f"""
    Transform this empty room into a realistic furnished {room}.
    
    Interior design style: {style}
    
    Requested furniture: {furniture}
    
    Requirements:
    - realistic furniture placement
    - correct shadows
    - proper perspective
    - modern interior design
    """

    try:

        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        image_base64 = result.data[0].b64_json

        return jsonify({
            "image": image_base64
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
