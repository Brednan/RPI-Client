from client import Client

client = Client('192.168.1.68', 65432)

res = client.send_request(b'Forward')
print(res.decode())