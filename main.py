import time
import socket
import time
from ultralytics import YOLO
import cv2
import pickle
import struct
import icecream as ic
from threading import Thread
#from receiver import receive, m
#from sender import send_text, connect
from sender2 import client
term = "Person"
check = True

def receive():
    global term
    def get_ip_address():
      global m
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(("8.8.8.8", 80))
      return s.getsockname()[0]


    # Socket creation
    cln_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host_ip = "172.20.10.2"
    print("ccheck")

    if host_ip == "y":
        host_ip = get_ip_address()

    time.sleep(1)
    print(f"Reciever IP {host_ip}")

    port = 9999
    socket_address = (host_ip, port)

    cln_sock.connect(socket_address)

    data = b""
    payload_size = struct.calcsize("Q")
    model = YOLO("yolov8l.pt")
    while True:
        global term
        while len(data) < payload_size:
            packet = cln_sock.recv(4*1024)
            if not packet:
                break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += cln_sock.recv(4*1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        #cv2.imshow("Recieved Video", frame)
        results = model(frame)
        names = model.names
        for r in results:
            for c in r.boxes.cls:
                term = names[int(c)]
                print(names[int(c)])

        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):
            break


def func1():
    print('Working func1')
    try:
        receive()
    except ConnectionRefusedError:
        print("Receive handshake Refused, retrying in 5 sec")
        time.sleep(5)
        func1()
    except ConnectionResetError:
        print("Connection Reset by other end, Start Sender Server")
        print("Retrying Connection in 10 sec")
        time.sleep(10)
        func1()



def func2():
    num = 1
    global term
    while True:
        try:
            print("Connected to receiver server(Func2)")
            term2 = term
            client.send_message(term)
            while True:
                if term != term2:
                    client.send_message(term)
                    term2 = term
                    time.sleep(0.5)
                    print(term)

        except:
            print("Connection Failure to send text")
            print("retying in 5 sec")
            time.sleep(5)

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target= func2).start()