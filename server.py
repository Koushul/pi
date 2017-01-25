from flask import Flask, request, render_template, jsonify
import bulb

app = Flask(__name__)


@app.route('/')

def index():
  return render_template('index.html')



@app.route('/setColor', methods=['POST'])
def setColor():
	#import bulb
	bulb.white(250)
	

if __name__ == '__main__':
	app.run(debug=True, host='128.151.85.124')
