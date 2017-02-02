import socket, time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def start():
    i = 0
    while(True):
	time.sleep(0.05)
        s = spectrum(i)
        i += 1
	sock.sendto(s, ("127.0.0.1", 8989) )	
	
def spectrum(offset):
    offset = offset % 100
    red = max(getVal(offset, 0), getVal(offset, 100))
    green = getVal(offset, 33)
    blue = getVal(offset, 67)
    return str(red) + "," + str(green) + "," +str(blue) + "," + str(255)

def getVal(offset, colPos):
    minO = colPos - 16.5
    maxO = colPos + 16.5
    
    if (offset > maxO):
        return max(min(255 - int(((offset - maxO) / 16.5) * 255), 255), 0)
    if (offset < minO):
        return max(min(255 - int(((minO - offset) / 16.5) * 255), 255), 0)

    return 255

start()
