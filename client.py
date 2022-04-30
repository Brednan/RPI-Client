from ctypes import sizeof
import socket
import time
import io
from PIL import Image

class Client:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(1.8)

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
    
    def request_footage(self):
        self.client.connect((self.HOST, self.PORT))
        self.client.sendall(b'Footage')

        footage_chunk = self.client.recv(2048)
        
        output_file = open('test.png', 'wb')
        
        while footage_chunk:
            output_file.write(footage_chunk)
            try:
                footage_chunk = self.client.recv(2048)
            except:
                break
