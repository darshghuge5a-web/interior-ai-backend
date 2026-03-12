from PIL import Image
import io


def resize_image(image):

    img = Image.open(image)

    img.thumbnail((1024, 1024))

    buffer = io.BytesIO()

    img.save(buffer, format="PNG")

    return buffer.getvalue()
