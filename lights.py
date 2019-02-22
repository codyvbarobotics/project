#Three lights Demo on and off
import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 4
all=[22,23,24]
redled = 22
yellowled = 23
greenled = 24
GPIO.setup(all,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(button,GPIO.IN,GPIO.PUD_UP)
time.sleep(2)
GPIO.output(redled,GPIO.HIGH)
time.sleep(3)
GPIO.output(yellowled,GPIO.HIGH)
time.sleep(3)
GPIO.output(greenled,GPIO.HIGH)
while GPIO.input(4):
    pass
for led in all:
    GPIO.output(led,GPIO.LOW)
    time.sleep(1)

