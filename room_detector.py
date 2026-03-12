import base64
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def detect_room(image):

    image_bytes = image.read()

    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    prompt = """
    Identify the room type in this image.

    Choose ONE from:
    bedroom
    living room
    kitchen
    bathroom
    office
    dining room
    empty room
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{base64_image}"
                }
            ]
        }]
    )

    return response.output_text.strip()
