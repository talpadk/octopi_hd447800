from RPLCD import CharLCD
import json, requests
import RPi.GPIO as GPIO  


PIN_BUTTON=3
PIN_A=5
PIN_B=7
DEBOUNCE=75

index_=0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_BUTTON, GPIO.IN)
GPIO.setup(PIN_A, GPIO.IN)
GPIO.setup(PIN_B, GPIO.IN)

lcd = CharLCD(pin_rw=None)

url = 'http://127.0.0.1/api/version'

def encoderCallback(pin):
	global index_
	if GPIO.input(PIN_B) :
		index_ -= 1
	else:
		index_ += 1
		
GPIO.add_event_detect(PIN_A, GPIO.FALLING, callback=encoderCallback, bouncetime=DEBOUNCE)  


params = dict(
    apikey=u'BA70ED98C4EB48E8B9D60B674AD46254',
)

resp = requests.get(url=url, params=params)

data = json.loads(resp.text)

lcd.write_string(u'OctoPrint HD447800')
lcd.cursor_pos = (1, 0)
lcd.write_string(u'API Ver: '+data['api'])
lcd.cursor_pos = (2, 0)
lcd.write_string(u'Server : '+data['server'])

while True:
	lcd.cursor_pos = (3, 13)
	if GPIO.input(PIN_BUTTON) :
		lcd.write_string("T%d  " % index_)
	else:
		lcd.write_string("F%d  " % index_)