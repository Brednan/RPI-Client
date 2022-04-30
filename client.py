import socket
import time

class Client:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #This function was made to test if the server was working
    def test_request(self):
        self.client.connect((self.HOST, self.PORT))
        self.client.sendall(b'Footage')
        time.sleep(1)
        return self.client.recv(1024)

    #This function sends a request to the server for it to move the motors forward
    def send_request(self, body:bytes):
        self.client.connect((self.HOST, self.PORT))
        self.client.sendall(body)
