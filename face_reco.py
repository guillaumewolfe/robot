import cv2

cap = cv2.VideoCapture(0)  # 0 is the default webcam

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()  # Read a frame
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw a green rectangle around each detected face
    for (x, y, w, h) in faces:
        increase_width = int(0.1 * w)
        increase_height = int(0.1 * h)
        
        x = x - increase_width // 2
        y = y - increase_height // 2
        w = w + increase_width
        h = h + increase_height
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('Webcam Feed', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()