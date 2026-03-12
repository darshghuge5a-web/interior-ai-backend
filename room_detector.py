import base64
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def detect_room(image):

    image_bytes = image.read()

    encoded = base64.b64encode(image_bytes).decode()

    prompt = """
Identify the room type in this image.

Return only ONE word from:
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
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{encoded}"
                    }
                ]
            }
        ]
    )

    return response.output_text.strip()
