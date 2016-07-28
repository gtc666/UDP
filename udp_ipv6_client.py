import socket

UDP_IP = "aaaa::212:4b00:a55:2a04"
#UDP_IP = "bbbb:0:0:0:a299:9bff:fe17:a21d"  # localhost
UDP_PORT = 7777
MESSAGE = "Hello, World!1"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET6, # Internet
					socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
recvData = sock.recvfrom(1024)
print "received message:", recvData[0]
print "from:", recvData[1]
