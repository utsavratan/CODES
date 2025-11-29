import cv2
import pytesseract

# If you have Tesseract installed locally, specify the path here
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load pre-trained Haar Cascade for license plate detection
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Initialize Video Capture (Live Camera)
cap = cv2.VideoCapture(0)  # Use 0 for default camera

# Set window size
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale (for better detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect number plates in the frame
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

    # Draw rectangles around detected number plates and recognize them
    for (x, y, w, h) in plates:
        # Draw rectangle around plate
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extract the number plate region from the frame
        plate_roi = frame[y:y + h, x:x + w]

        # Optional: Preprocess for better OCR accuracy (resize and grayscale)
        plate_gray = cv2.cvtColor(plate_roi, cv2.COLOR_BGR2GRAY)
        plate_resized = cv2.resize(plate_gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        # Use Tesseract to recognize text (number plate)
        plate_text = pytesseract.image_to_string(plate_resized, config='--psm 8')  # PSM 8 is for single word detection

        # Clean the OCR result
        plate_text = ''.join(e for e in plate_text if e.isalnum())  # Remove any non-alphanumeric characters

        # Display recognized text on the frame
        cv2.putText(frame, plate_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Real-Time Number Plate Detection', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
