from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (modify this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def detect_text(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    text = text.split('\n')
    return text

if __name__ == '__main__':
    # Detect text in image
    text = detect_text(r'C:\Users\HP\Desktop\Activity Monitoring Of Any Person\BACKEND\REDDIT\images\1.png')
    print(text)

    text = text.split('\n')
    print(text)
