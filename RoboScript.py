from flask import (Flask, request, jsonify, render_template)
import RPi.GPIO as gpio
import time

app = Flask(__name__)


def init():
  gpio.setmode(gpio.BOARD)
  gpio.setup(7, gpio.OUT)
  gpio.setup(11, gpio.OUT)
  gpio.setup(13, gpio.OUT)
  gpio.setup(15, gpio.OUT)

def driveForward(dt):
  gpio.output(7, True)
  gpio.output(11, False)
  gpio.output(13, False)
  gpio.output(15, True)
  time.sleep(dt)
  gpio.cleanup()

def driveReverse(dt):
  gpio.output(7, False)
  gpio.output(11, True)
  gpio.output(13, True)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def forwardRight(dt):
  gpio.output(7, True)
  gpio.output(11, False)
  gpio.output(13, False)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def forwardLeft(dt):
  gpio.output(7, False)
  gpio.output(11, False)
  gpio.output(13, False)
  gpio.output(15, True)
  time.sleep(dt)
  gpio.cleanup()

def reverseRight(dt):
  gpio.output(7, False)
  gpio.output(11, True)
  gpio.output(13, False)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def reverseLeft(dt):
  gpio.output(7, False)
  gpio.output(11, False)
  gpio.output(13, True)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def clockwise(dt):
  gpio.output(7, True)
  gpio.output(11, False)
  gpio.output(13, True)
  gpio.output(15, False)
  time.sleep(dt)
  gpio.cleanup()

def counterClockwise(dt):
  gpio.output(7, False)
  gpio.output(11, True)
  gpio.output(13, False)
  gpio.output(15, True)
  time.sleep(dt)
  gpio.cleanup()


@app.route("/")
def index():
  return render_template("index.html")

@app.route('/ajax', methods = ['POST'])
def ajax_request():
  username = request.form['username']
  return jsonify(username=username)
    
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)



