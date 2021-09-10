from flask import Flask, render_template, request
import pigpio
import smbus
import relay8

pi = pigpio.pi()
app = Flask(__name__)

RELAY1 = 1
RELAY2 = 2
RELAY3 = 3
RELAY4 = 4
RELAY5 = 5
RELAY6 = 6
RELAY7 = 7
RELAY8 = 8

r1stat = 1
r2stat = 1
r3stat = 1
r4stat = 1
r5stat = 1
r6stat = 1
r7stat = 1
r8stat = 1


BUTTON1 = 2
BUTTON2 = 3
BUTTON3 = 4
BUTTON4 = 5
BUTTON5 = 6
BUTTON6 = 7
BUTTON7 = 8
BUTTON8 = 9

#pi.set_mode(BUTTON1,pigpio.OUTPUT)
#pi.set_mode(BUTTON2,pigpio.OUTPUT)
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
        'RELAY1' : r1stat,
        'RELAY2' : r2stat,
        'RELAY3' : r3stat,
        'RELAY4' : r4stat,
        'RELAY5' : r5stat,
        'RELAY6' : r6stat,
        'RELAY7' : r7stat,
        'RELAY8' : r8stat,
    }
    return render_template('index8.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'RELAY1':
        relay = RELAY1
        button = BUTTON1
    if deviceName == 'RELAY2':
        relay = RELAY2
        button = BUTTON2
    if deviceName == 'RELAY3':
        relay = RELAY3
        button = BUTTON3
    if deviceName == 'RELAY4':
        relay = RELAY4
        button = BUTTON4
    if deviceName == 'RELAY5':
        relay = RELAY5
        button = BUTTON5
    if deviceName == 'RELAY6':
        relay = RELAY6
        button = BUTTON6
    if deviceName == 'RELAY7':
        relay = RELAY7
        button = BUTTON7
    if deviceName == 'RELAY8':
        relay = RELAY8
        button = BUTTON8

    if action == "on":
        relay8.set(0,1,1)
        pi.gpio_trigger(button,10,1)
    if action == "off":
        relay8.set(0,relay,0)

    r1stat = pi.read(RELAY1)
    r2stat = pi.read(RELAY2)
    r3stat = pi.read(RELAY3)
    r4stat = pi.read(RELAY4)
    r5stat = pi.read(RELAY5)
    r6stat = pi.read(RELAY6)
    r7stat = pi.read(RELAY7)
    r8stat = pi.read(RELAY8)

    templateData = {
        'RELAY1' : r1stat,
        'RELAY2' : r2stat,
        'RELAY3' : r3stat,
        'RELAY4' : r4stat,
        'RELAY5' : r5stat,
        'RELAY6' : r6stat,
        'RELAY7' : r7stat,
        'RELAY8' : r8stat,
    }
    return render_template('index8.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
