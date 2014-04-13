#!/usr/bin/env python

import doglcd, datetime, time

# __init__(self, lcdSI, lcdCLK, lcdRS, lcdCSB, pin_reset, pin_backlight):
# pin   wpi   bcm
# SI      2   27 rev 2, 21 rev 1
# CLK     3   22
# RS      5   24
# CSB     4   23
# RST    -1
# BL     -1
#
lcd = doglcd.DogLCD(21,22,24,23,-1,-1)
lcdb = doglcd.DogLCD(21,22,24,18,-1,-1)

lcd.begin(doglcd.DOG_LCD_M163, 0x28)
lcd.clear()
lcd.home()
lcd.doubleHeight()
lcd.doubleHeightTop()

lcdb.begin(doglcd.DOG_LCD_M163, 0x28)
lcdb.clear()
lcdb.home()
lcdb.doubleHeight()
lcdb.doubleHeightBottom()

lcdb.noCursor()
lcd.noCursor()

lcdb.setCursor(1,0)
lcdb.write('DOGE!!!')

while 1:
	lcd.setCursor(0,0)
	lcdb.setCursor(0,0)
	t = datetime.datetime.now().strftime("%H:%M:%S.%f")
	lcd.write(t)
	lcdb.write(t)
	lcd.setCursor(0,1)
	d = datetime.datetime.now().strftime("%Y-%m-%d")
	lcd.write(d)
	