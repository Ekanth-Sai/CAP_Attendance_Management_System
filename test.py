import cv2

# Open the default camera (usually the laptop's built-in camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open camera")
    exit()

# Capture a frame
ret, frame = cap.read()

# Check if the frame is captured successfully
if not ret:
    print("Error: Couldn't capture frame")
    cap.release()
    exit()

# Print the dimensions of the frame
print("Frame dimensions: {} x {}".format(frame.shape[1], frame.shape[0]))

# Release the camera
cap.release()
