import cv2
def detect_faces(image):
    # Create a cascade classifier object for the frontal face
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return image

def capture_video():
    # Initialize the video capture object
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open the camera")
        return

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while True:
        # Capture a frame-by-frame
        ret, frame = cap.read()

        # Break the loop if a frame is not read
        if not ret:
            break

        # Detect faces in the frame
        frame = detect_faces(frame)

        # Write the frame into the output video file
        out.write(frame)

        # Display the frame in a window
        cv2

capture_video