import locale
locale.setlocale(locale.LC_ALL, 'C')
import tesserocr
from PIL import Image

image = Image.open('code2.jpg')
result = tesserocr.image_to_text(image)
print(result)
