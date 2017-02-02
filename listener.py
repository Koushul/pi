import bulb
import socket
import webcolors

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',8989))
bulb.bulb.set_state(255,0,0,255)

def closest_color(requested_color):
	min_colors = {}
	for key, name in webcolors.css3_hex_to_names.items():
		r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        	rd = (r_c - requested_color[0]) ** 2
        	gd = (g_c - requested_color[1]) ** 2
        	bd = (b_c - requested_color[2]) ** 2
        	min_colors[(rd + gd + bd)] = name
    	return min_colors[min(min_colors.keys())]

def get_color_name(requested_color):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        closest_name = closest_color(requested_color)
        actual_name = None
    return actual_name, closest_name

while True:
	data, addr = sock.recvfrom(1024)
	data = data.split(",")
	bulb.bulb.set_state(int(data[0]), int(data[1]),int(data[2]),int(data[3]))

	
	#requested_color = (int(data[0]), int(data[1]),int(data[2]))
	
	#print ""
	#actual_name, closest_name = get_color_name(requested_color)
	#print "[!] Actual color name: ", actual_name
	#print "[!] Color: ", closest_name
	#print "[!] Brightness: ", (int(data[3])/255.0)*100, "%"



	print ""
	print "[~] Listening ... "
