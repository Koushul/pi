import bulb
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',8989))
bulb.bulb.set_state(255,0,0,255)

while True:
	data, addr = sock.recvfrom(1024)
	data = data.split(",")
	bulb.bulb.set_state(int(data[0]), int(data[1]),int(data[2]),int(data[3]))
	print "Bulb set by: ", addr	
	print ""
	print "[+] Listening ... "
