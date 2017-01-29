import RPi.GPIO as GPIO
import time as t
import keys as k
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)

timeout_ms = 2700
req_send = False
last_motion_time = 0



def send_IFTTT_Request(key):
	url = 'https://maker.ifttt.com/trigger/pir-motion-detect/with/key/' + key

	r = requests.get(url)	
	print(r.status_code)
	return


print 'Started.'

while True:
	if GPIO.input(4):
		last_motion_time = t.time()
		if (req_send == False and t.localtime().tm_hour >= 7 and t.localtime.tm_hour < 8):
			req_send = True
			#send IFTTT
			send_IFTTT_Request(k.IFTTT)
			print 'Request sent'

	if req_send == True:
		current_time = t.time()
		diff = current_time - last_motion_time 
		if diff > timeout_ms:
                	req_send = False
                        print 'Reset timeout'
