from client import Client

class Vision:
    def __init__(self) -> None:
        self.active = True
        client = Client('192.168.1.90', 65432)
        client.request_footage()

    def get_footage(self):
        client = Client('192.168.1.90', 65432)
        client.request_footage()