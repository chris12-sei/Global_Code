

from pprint import pprint
import requests 
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=96cefe7ad4be519263f4ea5dd72632b4')
pprint(r.json())
