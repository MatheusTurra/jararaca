try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """This function will handle the core OCR processing of images."""
    text = pytesseract.image_to_string(Image.open(filename))
    return text

print(ocr_core('images/ocr_example_1.png'))
