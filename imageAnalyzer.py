from io import BytesIO
from colorthief import ColorThief
import webcolors
import requests


class ImageAnalyzer:
    def __init__(self, image_url):
        self.image_url = image_url

    def get_color_palette(self, num_colors):
        # Descargar la imagen desde la URL usando requests
        response = requests.get(self.image_url)
        image_bytes = BytesIO(response.content)
        # Obtener los colores dominantes de la imagen
        color_thief = ColorThief(image_bytes)
        dominant_colors = color_thief.get_palette(color_count=num_colors, quality=10)
        hex_palette = []
        for color in dominant_colors:
            hex_color = webcolors.rgb_to_hex(color)
            hex_palette.append(hex_color)
        return hex_palette
