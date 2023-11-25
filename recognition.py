from ultralytics import YOLO
import cv2
# Load the pre-trained YOLOv8 model
model = YOLO('yolov8m.pt')

# Capture a video stream from the webcam
cap = cv2.VideoCapture(0)

# Loop over the video frames
while True:

    # Read the next video frame
    ret, frame = cap.read()

    # If the frame is empty, break the loop
    if not ret:
        break

    # Detect objects in the frame
    detections = model(frame)
    print(detections[0])
    # Loop over the detections
    for detection in detections:

        # Get the object class name and confidence score
        class_name = "detection[0]"
        print("------------")
        print("------------")
        confidence = "detection[1]"

        # Draw a bounding box around the object
        bounding_box = detection[2:6]
        #cv2.rectangle(frame, bounding_box, (0, 255, 0), 2)

        # Display the object class name and confidence score
        # cv2.putText(frame, class_name, (bounding_box[0], bounding_box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # cv2.putText(frame, str(confidence), (bounding_box[0], bounding_box[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the video frame
    cv2.imshow('Video', frame)

    # If the user presses the 'q' key, break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
