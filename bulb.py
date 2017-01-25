
import os,time,tikteck, random

bulb = tikteck.tikteck("00:21:4D:06:0B:70", "Smart Light", "241866259")

bulb.connect()


#bulb.set_state(230,0,255,255)

def set(r, g, b, a):
	bulb.set_state(r, g, b, a)

def ambient():
	bulb.set_state(230,0,255,255)

def white(b):
	bulb.set_state(255,255,255,b)

def night(brightness):
	bulb.set_state(255,92,0,brightness)

def dance(sleeptime):
	while 1:
		bulb.set_state(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),255)
		time.sleep(sleeptime)

def shiftambient():
	r = 0
	while 1:
		
		bulb.set_state(0,r,255,255)

	#	time.sleep(0.5)
		
		if (r==255):
			while (r > 0):
				bulb.set_state(0,r,255,255)
				#time.sleep(0.5)
				r=r-1
			
		r = r+1

		
def off():
	 bulb.set_state(0,0,0,0)
