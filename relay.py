import RPi.GPIO,time

GPIO.setmode(GPIO.BMC)
GPIO.setwarnings(FALSE)
red= 23
GPIO.setup(redled,GPIO.OUT,initial=GPIO.LOW)
GPIO.output(redled,GPIO.HIGH
time.sleep(5)
