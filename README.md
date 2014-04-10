DOG LCD Python for Raspberry Pi
===============================

Special thanks to Eberhard Fahle who created the Arduino DogLcd library
which I have ported to create this module.

Intro
-----

This library supports the DOGM081E, DOGM163E and DOGM183E displays with ST7036 driver IC over
the 4-wire SPI serial interface ( SI: Serial Input, CLK: Clock, RS: Register-Select and CSB: Chip-Select ).

You must connect at least SI, CLK and RS but can add multiple displays using an extra pin for each CSB.

Refer to the DOG LCD datasheet for details on wiring and support components for 3.3v SPI.

http://www.lcd-module.com/eng/pdf/doma/dog-me.pdf

Note: This library has only been tested against the DOGM163E-A

Getting Started
---------------

Install the doglcd module and use as follows:

    import doglcd
	
	CONTRAST = 0x28

    lcd = doglcd.DogLCD(SI, CLK, RS, CSB, RESET, BACKLIGHT)
    lcd.begin(doglcd.DOG_LCD_M163, CONTRAST)

	lcd.clear()
	lcd.home()

	lcd.write('Hello World!')


Usage
=====

reset()
-------
Reset the LCD

clear()
-------
Clear the LCD

home()
------
Relocate cursor to 0,0

noCursor() / cursor()
---------------------
Turn the cursor off / on

noDisplay() / display()
-----------------------
Turn the display off / on

noBlink() / blink()
-------------------
Turn blinking cursor off / on

scrollDisplayLeft() / scrollDisplayRight()
------------------------------------------
Manually scroll the display 1 character to the left or right

autoScroll() / noAutoscroll()
-----------------------------
Toggles on / off automatic scrolling

createChar(index,arr_char)
--------------------------
Create a new char at index ( 0 to 7 )
using an array of 8 5-bit numbers ( 0 to 31 )

Empty char:
    [0,0,0,0,0,0,0,0]

Full char:
	[31,31,31,31,31,31,31,31]

rightToLeft() / leftToRight()
-----------------------------
Change text direction

setContrast(contrast)
---------------------
Change the contrast
Valid values from 0 to 0x3F

writeChar(int)
--------------
Write a valid single char from 0 to 255

write(string/int)
-------------
Write a string or number to the LCD






Hardware setup
==============

DOG LCD Data Pinout
-------------------

TOP LEFT
40 : RST, Reset : Pull to VCC
39 : RS, Register Select ( Low = Command / High = Data ) -> Pi
38 : CSB, Chip Select -> Pi
37 : RW ( Low = Write / High = Read ) : Pull to GND
36 : E, Enable : Pull to VCC
35 : D0 : Pull to VCC
34 : D1 : Pull to VCC
33 : D2 : Pull to VCC
32 : D3 : Pull to VCC
31 : D4 : Pull to VCC
30 : D5 : Pull to VCC
29 : D6 : CLK, Clock -> Pi
28 : D7 : SI, Serial Input -> Pi
27 : GND
26 : VCC
25 : Voltage Booster IN : Pull to VCC
24 : Voltage Booster OUT : Bridge to 25 with 0.1uF Cap
23 : PSB ( Low = Serial / High = Parallel ) : Pull to GND
22 : Voltage Booster +
21 : Voltage Booster - : Bridge to 22 with 0.1uF Cap