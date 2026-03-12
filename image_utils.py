from PIL import Image
import io
from config import MAX_IMAGE_DIMENSION


def resize_image(image):

    img = Image.open(image)

    img.thumbnail((MAX_IMAGE_DIMENSION, MAX_IMAGE_DIMENSION))

    buffer = io.BytesIO()

    img.save(buffer, format="PNG")

    return buffer.getvalue()
