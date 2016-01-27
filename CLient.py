import socket
tcp = socket.gethostbyname(socket.gethostname())
port = 9001
buffer = 1024
message = "hello"
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((tcp,port))
s.send(message.encode(encoding='utf-8'))
print("sent")
s.close()