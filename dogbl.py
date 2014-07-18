# Sample script for PiGlow that creates a continuous whirly vortex animation
#
# Please see our GitHub repository for more information: https://github.com/pimoroni/piglow
#
# Once running you'll need to press ctrl-C to cancel stop the script

import time
from piglow import PiGlow
import colorsys

LED_R_R = 0x00
LED_R_B = 0x01
LED_R_G = 0x02

LED_M_R = 0x03
LED_M_B = 0x04
LED_M_G = 0x05

LED_L_R = 0x06
LED_L_B = 0x07
LED_L_G = 0x08

class DogBL(PiGlow):
	i2c_addr = 0x54 # fixed i2c address of SN3218 ic
	bus = None
	leds = [0x00] * 18

	def __init__(self, i2c_bus=1):
		PiGlow.__init__(self, i2c_bus)

	def setBar(self, index, value):
		for i, v in enumerate(value):
			self.leds[LED_L_G + 1 + index + i] = v
	
	def hue_to_rgb( self, hue ):
		rgb = colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)

		return [int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)]

	def hue( self, hue ):
		rgb = self.hue_to_rgb( hue )
		self.RGB( rgb[0], rgb[1], rgb[2] )

	def sweep( self, hue, range = 30 ):
		self.leftHue( (hue-range) % 360 )
		self.midHue( hue )
		self.rightHue( (hue+range) % 360 )

	def leftHue( self, hue ):
		rgb = self.hue_to_rgb( hue )
		self.leftRGB( rgb[0], rgb[1], rgb[2] )

	def midHue( self, hue ):
		rgb = self.hue_to_rgb( hue )
		self.midRGB( rgb[0], rgb[1], rgb[2] )

	def rightHue( self, hue ):
		rgb = self.hue_to_rgb( hue )
		self.rightRGB( rgb[0], rgb[1], rgb[2] )

	def leftRGB( self, r, g, b ):
		self.set(LED_L_R, r)
		self.set(LED_L_B, b)
		self.set(LED_L_G, g)

	def midRGB( self, r, g, b ):
		self.set(LED_M_R, r)
		self.set(LED_M_B, b)
		self.set(LED_M_G, g)

	def rightRGB( self, r, g, b ):
		self.set(LED_R_R, r)
		self.set(LED_R_B, b)
		self.set(LED_R_G, g)

	def RGB( self, r, g, b ):
		self.leftRGB( r, g, b )
		self.midRGB( r, g, b )
		self.rightRGB( r, g, b)

	def update(self):
		PiGlow.update(self)
