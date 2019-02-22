import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
redled= 23
GPIO.setup(redled,GPIO.OUT,initial=GPIO.LOW)
GPIO.output(redled,GPIO.HIGH)
time.sleep(5)
