import socket

# Set the socket parameters
addr = ('', 33333)  # host, port

# Create socket and bind to address
UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPSock.bind(addr)

# Receive messages
while True:
    data, addr = UDPSock.recvfrom(1024)
    if data == 'stop':
        print ('Client wants me to stop.')
        break
    else:
        print ("From addr: , msg: " + (addr[0], data))

UDPSock.close()
print ('Server stopped.')