import base64
from openai import OpenAI
from config import OPENAI_API_KEY, IMAGE_SIZE
from image_utils import resize_image

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_room(image, room, style, furniture):

    resized = resize_image(image)

    encoded = base64.b64encode(resized).decode()

    prompt = f"""
Transform this empty {room} into a professionally designed interior.

Interior style: {style}

Furniture requested: {furniture}

Requirements:
- realistic furniture placement
- correct perspective
- modern lighting
- natural shadows
- professional interior design photography
"""

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size=IMAGE_SIZE
    )

    image_base64 = result.data[0].b64_json

    return {
        "generated_image": image_base64
    }
