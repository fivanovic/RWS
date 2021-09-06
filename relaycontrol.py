from flask import Flask, render_template, request
import pigpio
pi = pigpio.pi()
app = Flask(__name__)

RELAY1 = 26
RELAY2 = 20
RELAY3 = 21

r1stat = 1
r2stat = 1
r3stat = 1

BUTTON1 = 2
BUTTON2 = 3
BUTTON3 = 4

pi.set_mode(RELAY1,pigpio.OUTPUT)
pi.set_mode(RELAY2,pigpio.OUTPUT)
pi.set_mode(RELAY3,pigpio.OUTPUT)

pi.set_mode(BUTTON1,pigpio.OUTPUT)
pi.set_mode(BUTTON2,pigpio.OUTPUT)
pi.set_mode(BUTTON3,pigpio.OUTPUT)

@app.route("/")
def index():
    templateData = {
        'title' : 'Relay Status',
        'RELAY1' : r1stat,
        'RELAY2' : r2stat,
        'RELAY3' : r3stat,

    }
    return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'RELAY1':
        relay = RELAY1
    if deviceName == 'RELAY2':
        relay = RELAY2
    if deviceName == 'RELAY3':
        relay = RELAY3

    if action == "on":
        pi.write(relay, 0)
    if action == "off":
        pi.write(relay, 1)

    r1stat = pi.read(RELAY1)
    r2stat = pi.read(RELAY2)
    r3stat = pi.read(RELAY3)

    templateData = {
        'RELAY1' : r1stat,
        'RELAY2' : r1stat,
        'RELAY3' : r1stat,
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
