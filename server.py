from flask import Flask, request, render_template, jsonify
import json, socket
from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('domain.key')
context.use_certificate_file('domain.crt')

#import os,time,tikteck, random

#bulb = tikteck.tikteck("00:21:4D:06:0B:70", "Smart Light", "241866259")

#def set(c):
#        bulb.set_state(c['r'], c['g'], c['b'], c['a'])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

app = Flask(__name__)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

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


@app.route('/on')
def on():
	sock.sendto("255,255,255,255", ("127.0.0.1", 8989))
        return json.dumps({'status' : 'Turning bulb on'})


@app.route('/off')
def off():
	
        sock.sendto("0,0,0,0", ("127.0.0.1", 8989))
	return json.dumps({'status' : 'Turning bulb off'})

	

@app.route('/ambient')
def ambient():
	sock.sendto("255,0,255,255", ("127.0.0.1", 8989))
	return json.dumps({'status' : 'Turning bulb purple'})	



if __name__ == '__main__':
	app.run(debug=True, host='128.151.85.124', ssl_context=context)
