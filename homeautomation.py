from flask import Flask
from flask import request

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)

@app.route('/led', methods=['GET','POST'])
def led():
        device = request.args.get('device')
        status = request.args.get('status')
        if status == "on":
           if device ==  "light1":
              light1On()
           else:
              light2On()
        else:
           if device ==  "light1":
              light1Off()
           else:
              light2Off()

        return "1"

def light1On():
    GPIO.output(18,GPIO.LOW)

def light1Off():
    GPIO.output(18,GPIO.HIGH)

def light2On():
    GPIO.output(15,GPIO.LOW)

def light2Off():
    GPIO.output(15,GPIO.HIGH)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
