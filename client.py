from ctypes import sizeof
import socket
import time
import io
from PIL import Image

class Client:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    #This function was made to test if the server was working
    def test_request(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.HOST, self.PORT))
        client.sendall(b'Footage')
        time.sleep(1)
        return client.recv(1024)

    #This function sends a request to the server with a specified message
    def send_request(self, body:bytes):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.HOST, self.PORT))
        client.sendall(body)
    
    #This function requests for the pictures that are taken by the Pi-Cam
    def request_footage(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1.8)
        client.connect((self.HOST, self.PORT))
        client.sendall(b'Footage')

        footage_chunk = client.recv(2048)
        
        output_file = open('./Vision/vision.png', 'wb')
        
        while footage_chunk:
            output_file.write(footage_chunk)
            try:
                footage_chunk = client.recv(2048)
            except:
                break
