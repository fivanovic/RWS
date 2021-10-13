import pigpio
import time
pi = pigpio.pi()
BUTTON1 = 10
BUTTON2 = 11
BUTTON3 = 12
BUTTON4 = 13
BUTTON5 = 14
BUTTON6 = 15
BUTTON7 = 16
BUTTON8 = 17

pi.set_mode(BUTTON1,pigpio.OUTPUT)
pi.set_mode(BUTTON2,pigpio.OUTPUT)
pi.set_mode(BUTTON3,pigpio.OUTPUT)
pi.set_mode(BUTTON4,pigpio.OUTPUT)
pi.set_mode(BUTTON5,pigpio.OUTPUT)
pi.set_mode(BUTTON6,pigpio.OUTPUT)
pi.set_mode(BUTTON7,pigpio.OUTPUT)
pi.set_mode(BUTTON8,pigpio.OUTPUT)

while True:

    pi.write(BUTTON1,10,1)
    print('Button on')
    time.sleep(5)
    pi.write(BUTTON1,10,0)
    print('Button off')
