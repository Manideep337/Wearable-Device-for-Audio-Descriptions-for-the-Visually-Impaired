import time
import subprocess
import cv2
from ultralytics import YOLO
from gtts import gTTS
from playsound import playsound
def play_audio(text):

    mytext = text
    myobj = gTTS(text=mytext, lang='en', slow=False)
    myobj.save("welcome.mp3")


model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    results = model(frame)# source already setup
    names = model.names

    for r in results:
        for c in r.boxes.cls:
            print(names[int(c)])
            print(names[int(c)])
            play_audio(names[int(c)])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break