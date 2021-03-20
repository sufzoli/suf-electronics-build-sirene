# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 160      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

"""
# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	# Wipe color across display a pixel at a time.
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	# Movie theater light style chaser animation.
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	# Generate rainbow colors across 0-255 positions.
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	# Draw rainbow that fades across all pixels at once.
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	# Draw rainbow that uniformly distributes itself across all pixels.
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	# Rainbow movie theater light style chaser animation.
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)
"""

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


# Main program logic follows:
if __name__ == '__main__':
	sirenLight(4,10)


"""
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	wipeLights(strip)
	while True:
		for i in range(0,15):
			stripColor(strip, Color(0, 0, 0), i)
			stripColor(strip, Color(0, 15, 0), (i+1) & 15)
			stripColor(strip, Color(0, 80, 0), (i+2) & 15)
			stripColor(strip, Color(0, 255, 0), (i+3) & 15)
			stripColor(strip, Color(0, 255, 0), (i+4) & 15)
			stripColor(strip, Color(0, 80, 0), (i+5) & 15)
			stripColor(strip, Color(0, 15, 0), (i+6) & 15)
			time.sleep(10/1000.0)
		stripColor(strip, Color(0, 0, 0), 15)
"""
	
