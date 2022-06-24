from flask import Flask, render_template, request
import pigpio
import smbus
import lib8relind
import time

#Defining a name for the GPIO control library
pi = pigpio.pi()
#Defining name for flask server
app = Flask(__name__)


class Relay:
    #This class defines the Relay object.
    #The object contains the unique ID, the relay number, the button it is assigned to control and its status
    def __init__(self, numb, button, status, id):
        self.numb = numb
        self.button = button
        self.status = status
        self.id = id

def toggle():
    #The toggle function forces all relays to turn off
    global R1
    global R2
    global R3
    global R4
    global R5
    global R6
    global R7
    global R8
    lib8relind.set(0,R1.numb,0)
    R1.status = "Off"
    lib8relind.set(0,R2.numb,0)
    R2.status = "Off"
    lib8relind.set(0,R3.numb,0)
    R3.status = "Off"
    lib8relind.set(0,R4.numb,0)
    R4.status = "Off"
    lib8relind.set(0,R5.numb,0)
    R5.status = "Off"
    lib8relind.set(0,R6.numb,0)
    R6.status = "Off"
    lib8relind.set(0,R7.numb,0)
    R7.status = "Off"
    lib8relind.set(0,R8.numb,0)
    R8.status = "Off"

def pusher(relay):
    #The pusher function updates the status of the relay currently being accessed
    global R1
    global R2
    global R3
    global R4
    global R5
    global R6
    global R7
    global R8
    if relay.numb == R1.numb:
        R1.status = relay.status
    elif relay.numb == R2.numb:
        R2.status = relay.status
    elif relay.numb == R3.numb:
        R3.status = relay.status
    elif relay.numb == R4.numb:
        R4.status = relay.status
    elif relay.numb == R5.numb:
        R5.status = relay.status
    elif relay.numb == R6.numb:
        R6.status = relay.status
    elif relay.numb == R7.numb:
        R7.status = relay.status
    elif relay.numb == R8.numb:
        R8.status = relay.status

RELAY1 = 8
RELAY2 = 7
RELAY3 = 6
RELAY4 = 5
RELAY5 = 4
RELAY6 = 3
RELAY7 = 2
RELAY8 = 1

BUTTON1 = 10
BUTTON2 = 11
BUTTON3 = 12
BUTTON4 = 13
BUTTON5 = 14
BUTTON6 = 15
BUTTON7 = 16
BUTTON8 = 17

#8 Relay objects are defined to match the 8 relays on the board
R1 = Relay(RELAY1,BUTTON1,"Off",1)
R2 = Relay(RELAY2,BUTTON2,"Off",2)
R3 = Relay(RELAY3,BUTTON3,"Off",3)
R4 = Relay(RELAY4,BUTTON4,"Off",4)
R5 = Relay(RELAY5,BUTTON5,"Off",5)
R6 = Relay(RELAY6,BUTTON6,"Off",6)
R7 = Relay(RELAY7,BUTTON7,"Off",7)
R8 = Relay(RELAY8,BUTTON8,"Off",8)

#The GPIO pins for the 8 buttons are set to output mode
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
    #a basic template for the status portion of the webserver
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
    #Points to the accessed relay based on the name and states what operation is being performed on it
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
        #all relays shut off
        toggle()
        #target relay is turned on
        lib8relind.set(0,relay.numb,1)
        #the 'button' is pressed for 1 second
        pi.write(relay.button,1)
        time.sleep(1)
        pi.write(relay.button,0)
        #relay status is updated
        relay.status = "On"
        #the status of the relay is pushed to its object
        pusher(relay)

    if action == "off":
        lib8relind.set(0,relay.numb,0)
        relay.status = "Off"
        pusher(relay)

    templateData = {
        #the template is updated with the updated status of all relays
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
    #running the flask server on  the local IP and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
