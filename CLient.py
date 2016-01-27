import socket
tcp = "192.168.0.101"
port = 5005
buffer = 1024
message = "hello"
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((tcp,port))
s.send(message.encode(encoding='utf-8'))
print("sent")
s.close()