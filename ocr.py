import cv2
import pytesseract

# Path to tesseract executable (for Windows users)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding (optional for better results)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Optionally apply noise removal or other preprocessing techniques
    # gray = cv2.medianBlur(gray, 3)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(gray)

    return text

# Test the function
if __name__ == "__main__":
    image_path = 'Images/doc2.jpg'
    extracted_text = extract_text(image_path)
    print("Extracted Text: \n", extracted_text)
