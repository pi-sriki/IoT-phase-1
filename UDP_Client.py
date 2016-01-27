import socket


#addr = ('localhost', 33333)                                # localhost, port
#addr = ('127.0.0.1', 33333)                                # localhost explicitly
#addr = ('xyz', 33333)                                      # explicit computer
#addr = ('<broadcast>', 33333)                              # broadcast address
addr = ('255.255.255.255', 33333)                          # broadcast address explicitly

UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create socket

print ('Enter your message:')
print ('- Empty message to stop this client.')
print ('- "stop" to stop all servers.')

# Almost infinite loop... ;)
while True:
    data = input('>> ')
    if len(data) == 0:
        break
    else:
        if UDPSock.sendto(data.encode(encoding='utf-8'), addr):
            print ("Sending message ..." + data)

UDPSock.close()             # Close socket
print ('Client stopped.')