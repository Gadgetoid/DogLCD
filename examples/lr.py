import doglcd, time, datetime, math

BORDER_TOP = 0
BORDER_BOTTOM = 1
BORDER_LEFT = 2
BORDER_RIGHT = 3
BORDER_TL = 4
BORDER_TR = 5
BORDER_BL = 6
BORDER_BR = 7

l = doglcd.DogLCD(21,22,24,18,-1,-1)
r = doglcd.DogLCD(21,22,24,23,-1,-1)

_ = 32


buf_l = [
	4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
	2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,
	6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

buf_r = [
	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,
	_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,3,
	1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7]


def initialise(disp):
	disp.begin(doglcd.DOG_LCD_M163, 0x28)
	disp.clear()
	disp.home()
	disp.noCursor()
	disp.noDoubleHeight()

	disp.createChar(BORDER_TOP,[31,31,0,0,0,0,0,0]) # Top

	disp.createChar(BORDER_TL,[31,31,24,24,24,24,24,24]) # Top Left
	disp.createChar(BORDER_BL,[24,24,24,24,24,24,31,31]) # Bottom Left

	disp.createChar(BORDER_TR,[31,31,3,3,3,3,3,3]) # Top Right
	disp.createChar(BORDER_BR,[3,3,3,3,3,3,31,31]) # Bottom Right
	
	disp.createChar(BORDER_LEFT,[24,24,24,24,24,24,24,24]) # Left
	disp.createChar(BORDER_RIGHT,[3,3,3,3,3,3,3,3]) # Right

	disp.createChar(BORDER_BOTTOM,[0,0,0,0,0,0,31,31]) # Bottom

	disp.home()


initialise(l)
initialise(r)


#for x in buf_l:
#	l.writeChar(x)
#for x in buf_r:
#	r.writeChar(x)

while 1:
	l.setCursor(0,0)
	r.setCursor(0,0)

	x = 1
	t = datetime.datetime.now().strftime("%H:%M:%S.%f")
	for letter in "This is a long piece of text which omg " + t + " such LCDs and wrap perfectly like magic oh wow and now overflow":
		if( x <= 96 ):
			if( math.ceil(float(x)/16.0) % 2 == 0 ):
				r.write(letter)
			else:
				l.write(letter)
		x+=1

while 1:
	l.setCursor(1,1)
	r.setCursor(0,1)
	x = 0
	for letter in "Hello World! It's " + datetime.datetime.now().strftime("%H:%M:%S.%f"):
		if( x < 30 ):
			if( x < 15):
				l.write(letter)
			else:
				r.write(letter)
			x+=1
