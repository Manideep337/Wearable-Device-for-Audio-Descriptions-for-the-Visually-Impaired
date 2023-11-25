import socket
sock = ''
def connect():
  ip_address = "172.20.10.2"
  port =   8080
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((ip_address, port))


def send_text(message):
  sock.sendall(message.encode())

