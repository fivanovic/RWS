from flask import Flask, render_template, request
import pigpio
import smbus
import lib8relind

pi = pigpio.pi()
app = Flask(__name__)

class Relay:
    def __init__(self, numb, button, status, id):
        self.numb = numb
        self.button = button
        self.status = status
        self.id = id

RELAY1 = 1
RELAY2 = 2
RELAY3 = 3
RELAY4 = 4
RELAY5 = 5
RELAY6 = 6
RELAY7 = 7
RELAY8 = 8

BUTTON1 = 10
BUTTON1 = 11
BUTTON1 = 12
BUTTON1 = 13
BUTTON1 = 14
BUTTON1 = 15
BUTTON1 = 16
BUTTON1 = 17

R1 = Relay(RELAY1,BUTTON1,"Off",1)
R2 = Relay(RELAY2,BUTTON2,"Off",2)
R3 = Relay(RELAY3,BUTTON3,"Off",3)
R4 = Relay(RELAY4,BUTTON1,"Off",4)
R5 = Relay(RELAY5,BUTTON2,"Off",5)
R6 = Relay(RELAY6,BUTTON3,"Off",6)
R7 = Relay(RELAY7,BUTTON1,"Off",7)
R8 = Relay(RELAY8,BUTTON2,"Off",8)


pi.set_mode(BUTTON1,pigpio.OUTPUT)
pi.set_mode(BUTTON2,pigpio.OUTPUT)
pi.set_mode(BUTTON3,pigpio.OUTPUT)
pi.set_mode(BUTTON4,pigpio.OUTPUT)
pi.set_mode(BUTTON5,pigpio.OUTPUT)
pi.set_mode(BUTTON6,pigpio.OUTPUT)
pi.set_mode(BUTTON7,pigpio.OUTPUT)
pi.set_mode(BUTTON8,pigpio.OUTPUT)


@app.route("/")
def index():
    templateData = {
        'title' : 'Relay Status',
        'RELAY1' : R1.status,
        'RELAY2' : R2.status,
        'RELAY3' : R3.status,
        'RELAY4' : R4.status,
        'RELAY5' : R5.status,
        'RELAY6' : R6.status,
        'RELAY7' : R7.status,
        'RELAY8' : R8.status,
    }
    return render_template('index8.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'RELAY1':
        relay = R1
    if deviceName == 'RELAY2':
        relay = R2
    if deviceName == 'RELAY3':
        relay = R3
    if deviceName == 'RELAY4':
        relay = R4
    if deviceName == 'RELAY5':
        relay = R5
    if deviceName == 'RELAY6':
        relay = R6
    if deviceName == 'RELAY7':
        relay = R7
    if deviceName == 'RELAY8':
        relay = R8

    if action == "on":
        lib8relind.set(0,relay.numb,1)
        pi.gpio_trigger(relay.button,10,1)
        relay.status = "On"

    if action == "off":
        lib8relind.set(0,relay.numb,0)
        relay.status = "Off"

    templateData = {
        'RELAY1' : R1.status,
        'RELAY2' : R2.status,
        'RELAY3' : R3.status,
        'RELAY4' : R4.status,
        'RELAY5' : R5.status,
        'RELAY6' : R6.status,
        'RELAY7' : R7.status,
        'RELAY8' : R8.status,
    }
    return render_template('index8.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
