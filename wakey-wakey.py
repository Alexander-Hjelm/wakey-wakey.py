import RPi.GPIO as gpio
import time
import datetime

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.OUT)

alarm_time_h = 25
alarm_time_m = 61

ringing = False

with open("time") as f:
	content = f.readlines()[0].split(":")
	alarm_time_h = int(content[0])
	alarm_time_m = int(content[1])

#print("Alarm will ring at: " + str(alarm_time_h) + ":" + str(alarm_time_m))

while True:

	if ringing:
		#print("Wake up!")
		gpio.output(4,1)
		time.sleep(1.5)
		gpio.output(4,0)
		time.sleep(3)
	else:
		now = datetime.datetime.now()
		#print("Current time is: " + str(now.hour) + ":" + str(now.minute))

		if now.hour == alarm_time_h and now.minute == alarm_time_m:
			ringing = True
		else:
			time.sleep(10)
