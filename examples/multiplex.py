import doglcd, time

l = doglcd.DogLCD(21,22,24,18,-1,-1)
r = doglcd.DogLCD(21,22,24,23,-1,-1)

def initialise(disp):
	disp.begin(doglcd.DOG_LCD_M163, 0x28)
	disp.clear()
	disp.home()
	disp.noCursor()

initialise(l)
initialise(r)


while 1:
	l.setCursor(1,1)
	l.writeChar(32)
	l.createChar(0,[24,24,24,24,24,24,24,24])
	l.home()
	l.writeChar(0)
	time.sleep(0.02)
	l.createChar(0,[3,3,3,3,3,3,3,3])	
	l.home()
	l.writeChar(32)
	l.setCursor(1,1)
	l.writeChar(0)
	time.sleep(0.02)