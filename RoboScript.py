from flask import (Flask, request, jsonify, render_template)
import json
import RPi.GPIO as gpio
import time

app = Flask(__name__)


def init():
  gpio.setmode(gpio.BOARD)
  gpio.setup(7, gpio.OUT)
  gpio.setup(11, gpio.OUT)
  gpio.setup(13, gpio.OUT)
  gpio.setup(15, gpio.OUT)

def driveForward():
  init()
  gpio.output(7, True)
  gpio.output(11, False)
  gpio.output(13, False)
  gpio.output(15, True)

def driveReverse():
  init()
  gpio.output(7, False)
  gpio.output(11, True)
  gpio.output(13, True)
  gpio.output(15, False)

def forwardRight():
  init()
  gpio.output(7, True)
  gpio.output(11, False)
  gpio.output(13, False)
  gpio.output(15, False)

def forwardLeft():
  init()
  gpio.output(7, False)
  gpio.output(11, False)
  gpio.output(13, False)
  gpio.output(15, True)

def reverseRight():
  init()
  gpio.output(7, False)
  gpio.output(11, True)
  gpio.output(13, False)
  gpio.output(15, False)

def reverseLeft():
  init()
  gpio.output(7, False)
  gpio.output(11, False)
  gpio.output(13, True)
  gpio.output(15, False)

def clockwise():
  init()
  gpio.output(7, True)
  gpio.output(11, False)
  gpio.output(13, True)
  gpio.output(15, False)  

def counterClockwise():
  init()
  gpio.output(7, False)
  gpio.output(11, True)
  gpio.output(13, False)
  gpio.output(15, True)


@app.route("/")
def index():
  return render_template("index.html")

@app.route('/ajax', methods = ['POST'])
def ajax():
  json_dict = request.get_json()
  data = json_dict['command']
  if data == 'driveForward':
    driveForward(3)
  elif data == 'driveReverse':
    driveReverse(3)
  elif data == 'forwardRight':
    forwardRight(3)
  elif data == 'forwardLeft':
    forwardLeft(3)
  elif data == 'reverseRight':
    reverseRight(3)
  elif data == 'reverseLeft':
    reverseLeft(3)
  elif data == 'clockwise':
    clockwise(3)
  elif data == 'counterClockwise':
    counterClockwise()
  elif data == 'stop':
    init()
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.cleanup()
    
  return json.dumps(request.json)
    
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)



