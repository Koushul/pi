from flask import Flask, request, render_template, jsonify
import json, socket

#import os,time,tikteck, random

#bulb = tikteck.tikteck("00:21:4D:06:0B:70", "Smart Light", "241866259")

#def set(c):
#        bulb.set_state(c['r'], c['g'], c['b'], c['a'])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

app = Flask(__name__)


@app.route('/')

def index():
  return render_template('index.html')


#def connect():
#	bulb.connect()

@app.route('/setColor', methods=['POST'])

def setColor():
	color = request.get_json()
	a = str(int(color['a']*255))
	nColor = { 'r': color['r'], 'g': color['g'], 'b': color['b'], 'a':a }
	data = str(color['r']) + "," + str(color['g']) + "," + str(color['b']) + "," + str(a)
	sock.sendto(data, ("127.0.0.1", 8989))
	#set(nColor)
	return json.dumps({'status' : 'OK', 'color': nColor}) 


def on():
	connect()
	bulb.set_state(255,255,255,255)

def off():
	connect()
	bulb.set_state(0,0,0,0)
	


if __name__ == '__main__':
	app.run(debug=True, host='128.151.85.124')
