import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 1234
client.connect((host,port))

while True:
    data = client.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    client.send(input().encode("utf-8"))
