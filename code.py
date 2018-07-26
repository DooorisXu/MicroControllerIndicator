# CircuitPlaygroundExpress_NeoPixel

import time

import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

# define some colors (R,G,B) / (255,255,255)
RED = 0x100000  # (0x10, 0, 0) also works
YELLOW = (0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)
CUSTOM_COLOR=(100,100,0)

def red_light_stop():
	pixels[0]=RED
	pixels[1]=RED
	pixels[2]=RED
	pixels[3]=RED
	pixels[4]=RED
	pixels[5]=RED
	pixels[6]=RED
	pixels[7]=RED
	pixels[8]=RED
	pixels[9]=RED

def yellow_light_yield():
	pixels[2]=YELLOW
	pixels[3]=YELLOW
	pixels[4]=YELLOW
	pixels[5]=YELLOW
	pixels[6]=YELLOW
	pixels[7]=YELLOW

def green_light_go():
	pixels[4]=GREEN
	pixels[5]=GREEN

def not_at_stoplight():
	pixels[0]=BLACK
	pixels[1]=BLACK
	pixels[2]=BLACK
	pixels[3]=BLACK
	pixels[4]=BLACK
	pixels[5]=BLACK
	pixels[6]=BLACK
	pixels[7]=BLACK
	pixels[8]=BLACK
	pixels[9]=BLACK

#the indicator will receive the feed from 
feed = 3

if feed == 1:
	green_light_go()
elif feed == 2:
	yellow_light_yield()
elif feed == 3:
	red_light_stop()
else:
	not_at_stoplight()


