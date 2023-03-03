from webScraper import WebScraper
from imageAnalyzer import ImageAnalyzer



# Crear una instancia del scraper web y obtener la URL de la imagen
url = "https://www.instagram.com/p/CmUv48DLvxd/"
scraper = WebScraper(url)
image_url = scraper.get_image_url()

# Crear una instancia del analizador de imágenes y obtener la paleta de colores
analyzer = ImageAnalyzer(image_url)
palette = analyzer.get_color_palette(10)

# Imprimir la paleta de colores
print("Paleta de colores:")
print(palette)

