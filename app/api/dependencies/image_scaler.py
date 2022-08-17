import io
import base64

from PIL import Image


def encode_image(raw_image: bytes):
    return base64.b64encode(raw_image)


def decode_image(encoded_image: str):
    return base64.b64decode(encoded_image)


def scale_image(image_data: bytes, target_width: int, target_height: int):
    image_data = Image.open(io.BytesIO(image_data))
    target_size = (target_width, target_height)
    resized_image = image_data.resize(target_size)
    return resized_image
