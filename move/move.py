#import RPi.GPIO as gpio
from gpiozero import Robot
import curses
import time

r = Robot(left=(7,8), right=(9,10))

def Move(dir, t, speed):
	if (speed == None):
		speed = 0.5
	if (t == None):
		t = 1

	print('moving ' + dir)

	if (dir == 'f'):
		r.forward(speed)
	elif (dir == 'b'):
		r.backward(speed)
	elif (dir == 'l'):
		r.left(speed)
	elif (dir == 'r'):
		r.right(speed)
	time.sleep(t)
	r.stop()
	time.sleep(0.25)


#actions = {
#	curses.KEY_UP: r.forward,
#	curses.KEY_DOWN: r.backward,
#	curses.KEY_LEFT: r.left,
#	curses.KEY_RIGHT: r.right
#}


def main(window):
	next_key = None
	key = None
	while True:
		curses.halfdelay(1)
		if next_key is None:
			key = window.getch()
		else:
			key = next_key
			next_key = None
		if key != -1:
			#keypress
			curses.halfdelay(1)
			action = actions.get(key)
			if action is not None:
				action(0.5)
			next_key = key
			while next_key == key:
					next_key = window.getch()
			#release
			r.stop()