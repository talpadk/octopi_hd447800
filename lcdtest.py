from RPLCD import CharLCD
import json, requests

lcd = CharLCD(pin_rw=None)

url = 'http://127.0.0.1/api/version'

params = dict(
    apikey=u'BA70ED98C4EB48E8B9D60B674AD46254',
)

resp = requests.get(url=url, params=params)

print resp
print resp.url

data = json.loads(resp.text)

lcd.write_string(u'OctoPrint HD447800')
lcd.cursor_pos = (1, 0)
lcd.write_string(u'API Ver: '+data['api'])
lcd.cursor_pos = (2, 0)
lcd.write_string(u'Server : '+data['server'])
