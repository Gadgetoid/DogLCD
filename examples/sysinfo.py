import doglcd, psutil, time, datetime, math

import socket, fcntl, struct

def get_ip_address(ifname):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
										0x8915, # SIOCGIFADDR
										struct.pack('256s', ifname[:15])
									)[20:24])
	except IOError:
		return ifname + ' not found!'

lcd = doglcd.DogLCD(21,22,24,18,-1,-1)

# Testing rig only, remove for production
# second LCD goes potty if you don't
# pull down its CSB pin!
alt = doglcd.DogLCD(21,22,24,23,-1,-1)
alt.begin(doglcd.DOG_LCD_M163, 0x28)
alt.clear()
alt.home()
alt.noCursor()
alt.noDoubleHeight()
alt.noAutoscroll()

lcd.begin(doglcd.DOG_LCD_M163, 0x28)
lcd.clear()
lcd.home()
lcd.noCursor()
lcd.noDoubleHeight()
lcd.noAutoscroll()

DOG_LCD_CHEVRON_L = 0b11111011
DOG_LCD_CHEVRON_R = 0b11111100

# We need some custom characters to
# complete the levels of bar graph
lcd.createChar(6,[0,31,0,0,0,0,0,0])
lcd.createChar(5,[0,0,31,0,0,0,0,0])
lcd.createChar(4,[0,0,0,0,31,0,0,0])
lcd.createChar(3,[0,0,0,0,0,31,0,0])
lcd.createChar(2,[0,0,0,0,0,0,0,31])

# Always call home after creating
# custom chars
lcd.home()

# Map out the levels of bar graph
graph_steps = [2,95,3,4,45,5,6,255]

graph_text = []

while 1:
	alt.setCursor(0,0)
	alt.write(get_ip_address('eth0'))

	alt.setCursor(0,1)
	alt.write(get_ip_address('wlan0'))

	ip = psutil.net_connections(kind='inet4')
	mem = psutil.virtual_memory()
	cpu = psutil.cpu_percent()

	lcd.setCursor(0,0)
	lcd.write("FREE " + str(mem.available/1024/1024) + 'MB/' + str(mem.total/1024/1024) + 'MB')

	lcd.setCursor(0,1)
	lcd.write("CPU% " + str(round(cpu,2)) + '    ')

	idx = int(math.floor((7.0/100.0) * cpu))
	
	graph_text.append(graph_steps[idx])

	if len(graph_text) > 16:
		graph_text.pop(0)

	lcd.setCursor(0,2)
	for char in graph_text:
		lcd.writeChar(char)

	time.sleep(0.25)