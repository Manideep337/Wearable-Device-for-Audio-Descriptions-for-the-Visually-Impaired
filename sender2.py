import socket

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('172.20.10.2', 12345)
        self.connect_to_server()

    def connect_to_server(self):
        # Connect to the server
        self.client_socket.connect(self.server_address)
        print("Connected to the server.")

    def send_message(self, message):
        # Send the message
        self.client_socket.sendall(message.encode('utf-8'))
        print(f"Sent message: {message}")

# Example usage
client = Client()

# Send messages whenever needed
client.send_message("Hello, server!")
#client.send_message("How are you?")
#client.send_message("This is another messa266ge.")

# To close the connection when done
# client.client_socket.close()
