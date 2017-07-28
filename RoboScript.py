from flask import (Flask, request, jsonify, render_template)
import json

"""
import RPi.GPIO as gpio
import time
"""
app = Flask(__name__)

"""
def init():
  gpio.setmode(gpio.BOARD)
  gpio.setup(7, gpio.OUT)
  gpio.setup(11, gpio.OUT)
  gpio.setup(13, gpio.OUT)
  gpio.setup(15, gpio.OUT)

def driveForward(dt):
  init()
  gpio.output(7, True)
  gpio.output(11, False)
  gpio.output(13, False)
  gpio.output(15, True)
  time.sleep(dt)
  gpio.cleanup()

def driveReverse(dt):
  init()
  gpio.output(7, False)
  gpio.output(11, True)
  gpio.output(13, True)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def forwardRight(dt):
  init()
  gpio.output(7, True)
  gpio.output(11, False)
  gpio.output(13, False)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def forwardLeft(dt):
  init()
  gpio.output(7, False)
  gpio.output(11, False)
  gpio.output(13, False)
  gpio.output(15, True)
  time.sleep(dt)
  gpio.cleanup()

def reverseRight(dt):
  init()
  gpio.output(7, False)
  gpio.output(11, True)
  gpio.output(13, False)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def reverseLeft(dt):
  init()
  gpio.output(7, False)
  gpio.output(11, False)
  gpio.output(13, True)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def clockwise(dt):
  init()
  gpio.output(7, True)
  gpio.output(11, False)
  gpio.output(13, True)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def counterClockwise(dt):
  init()
  gpio.output(7, False)
  gpio.output(11, True)
  gpio.output(13, False)
  gpio.output(15, True)
  time.sleep(dt)
  gpio.cleanup()
  
  """


@app.route("/")
def index():
  return render_template("index.html")

@app.route('/ajax', methods = ['POST'])
def ajax():
  json_dict = request.get_json()
  data = json_dict['command']
  if data == 'driveForward':
    driveForward(1000)
  elif data == 'driveReverse':
    driveReverse(1000)
  elif data == 'forwardRight':
    forwardRight(1000)
  elif data == 'forwardLeft':
    forwardLeft(1000)
  elif data == 'reverseRight':
    reverseRight(1000)
  elif data == 'reverseLeft':
    reverseLeft(1000)
  elif data == 'clockwise':
    clockwise(1000)
  elif data == 'counterClockwise':
    counterClockwise(1000)
  elif data == 'stop':
    gpio.cleanup()
    
  return json.dumps(request.json)
    
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)



