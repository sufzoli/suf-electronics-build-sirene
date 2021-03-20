import requests
import configparser
import time
from neopixel import *
from  datetime import datetime

# LED strip configuration:
LED_COUNT      = 160      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

def stripColor(strip,color,stripNum):
	for i in range(stripNum * 10, (stripNum + 1) * 10):
		strip.setPixelColor(i,color)
	strip.show()

def wipeLights(strip):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0, 0, 0))
	strip.show()

def sirenLight(sirenColor,roundNum):
	r = sirenColor & 1
	g = (sirenColor >> 1) & 1
	b = (sirenColor >> 2) & 1
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	wipeLights(strip)
	for j in range(1,roundNum):
		for i in range(0,15):
			stripColor(strip, Color(0, 0, 0), i)
			stripColor(strip, Color(r *  15, g *  15, b *  15), (i+1) & 15)
			stripColor(strip, Color(r *  80, g *  80, b *  80), (i+2) & 15)
			stripColor(strip, Color(r * 255, g * 255, b * 255), (i+3) & 15)
			stripColor(strip, Color(r * 255, g * 255, b * 255), (i+4) & 15)
			stripColor(strip, Color(r *  80, g *  80, b *  80), (i+5) & 15)
			stripColor(strip, Color(r *  15, g *  15, b *  15), (i+6) & 15)
			time.sleep(10/1000.0)
		stripColor(strip, Color(0, 0, 0), 15)
	wipeLights(strip)


class Build:
    def __init__(self, key, num, state, completeddt):
        self.key = key
        self.num = num
        self.state = state
        self.completeddt = completeddt

ini = configparser.ConfigParser()
#ini.read('C:/DATA/TEST/BuildSiren/buildsiren.cfg')
ini.read('/etc/buildsiren/buildsiren.conf')

url = ini.get('config','url')
user = ini.get('config','user')
pwd = ini.get('config','pwd')

completedon = datetime.min

# Get the list of builds
r = requests.get(url + '/rest/api/latest/result.json?os_authType=basic&max-results=1000', auth=(user, pwd))
bamboodata = r.json()

# iterate through the build the find the latest
# this will be the base build will generate no event
for i in range(0, bamboodata['results']['max-result']):
    planurl = bamboodata['results']['result'][i]['link']['href'] + '.json?os_authType=basic'
    planresult = requests.get(planurl,  auth=(user, pwd))
    planjson = planresult.json()
    if completedon < datetime.strptime(planjson['buildCompletedDate'], '%Y-%m-%dT%H:%M:%S.%fZ'):
        completedon = datetime.strptime(planjson['buildCompletedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
        plankey = planjson['plan']['key']
        buildnum = planjson['buildNumber']
        buildstate = planjson['state']
    # print(str(complettedon) + ',' + planjson['plan']['key'] + ',' + str(planjson['buildNumber']) + ',' + planjson['state'])

print(str(completedon) + ',' + plankey + ',' + str(buildnum) + ',' + buildstate)

while True:
    # Get the list of builds
    r = requests.get(url + '/rest/api/latest/result.json?os_authType=basic&max-results=1000', auth=(user, pwd))
    bamboodata = r.json()

    buildlist = []

    # iterate through the build the find the newer builds
    for i in range(0, bamboodata['results']['max-result']):
        planurl = bamboodata['results']['result'][i]['link']['href'] + '.json?os_authType=basic'
        planresult = requests.get(planurl,  auth=(user, pwd))
        planjson = planresult.json()
        if completedon < datetime.strptime(planjson['buildCompletedDate'], '%Y-%m-%dT%H:%M:%S.%fZ'):
            print(str(datetime.strptime(planjson['buildCompletedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')) + ',' + planjson['plan']['key'] + ',' + str(planjson['buildNumber']) + ',' + planjson['state'])
            buildlist.append(Build(planjson['plan']['key'], planjson['buildNumber'], planjson['state'], datetime.strptime(planjson['buildCompletedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')))

    for i in range(0, len(buildlist)):
        print(str(i) + ',' +  str(buildlist[i].completeddt))
        if completedon < buildlist[i].completeddt:
            completedon = buildlist[i].completeddt
        if buildstate == 'Successful':
            sirenLight(2,10)
        else:
            sirenLight(1,10)

