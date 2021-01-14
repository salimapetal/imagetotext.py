try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core():
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open('/Users/salimakazab/Desktop/petalwinternproject2021/uploads/utilitybill.jpg'))  #image to text works
    return text

if __name__ == "__main__" :
    print(ocr_core())

