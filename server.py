from flask import Flask, request, render_template, jsonify
import json

import os,time,tikteck, random

bulb = tikteck.tikteck("00:21:4D:06:0B:70", "Smart Light", "241866259")

def set(r, g, b, a):
        bulb.set_state(r, g, b, a)

app = Flask(__name__)


@app.route('/')

def index():
  return render_template('index.html')


def connect():
	bulb.connect()

@app.route('/setColor', methods=['POST'])

def setColor():
	connect()
	color = request.get_json()
	a = color['a']*255
	set(color['r'], color['g'], color['b'], a)
	return json.dumps({'status' : 'OK', 'color': color}) 


if __name__ == '__main__':
	app.run(debug=True, host='128.151.85.124')
