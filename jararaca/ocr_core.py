try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    with Image.open(filename) as img:
        img = img.convert('L')
        text = pytesseract.image_to_string(img.resize((img.size[0]*4, img.size[1]*4)), lang='por')
    return text
