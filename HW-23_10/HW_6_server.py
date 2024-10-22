import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))
server.listen()

user, addres = server.accept()
print("connect")

while True:
    user.send(input().encode("utf-8"))
    data = user.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
