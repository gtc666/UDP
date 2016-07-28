import socket
  
UDP_IP = "::" # = 0.0.0.0 u IPv4
UDP_PORT = 7777

sock = socket.socket(socket.AF_INET6, # Internet
						socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
	print "from:", addr
	sock.sendto("server response",(addr[0],addr[1]))
