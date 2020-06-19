bootCmds = input("Boot Options: ")

print("Booting...")

if ('-s' not in bootCmds):
	print('Loading Speech')
	from speech.speak import Say
if ('-h' not in bootCmds):
	#print('Loading Hearing')
	print("h")
	#from recognition.speech import sr
if ('-m' not in bootCmds):
	print('Loading Movement')
	from move.move import Move

print("Boot Complete, Please Wait...")

#sense & motion handlers
def say(text):
	try:
		Say(text)
	except:
		print('Speech Attempted; Module Disabled')

def move(dir, t, speed):
	try:
		Move(dir, t, speed)
	except:
		print("Movement Module Disabled")

def main():

	try:
		say("Awaiting Instructions")
	except:
		print('Speech Module Disabled')
	while True:
		cmd = input()

		#hard coded commands
		if (cmd == 'shutdown'):
			say("Shutting Down")
			exit()
		elif (cmd == 'say'):
			say(input())
		elif (cmd == 'move'):
			move('l', 1, 0.75)
			move('r', 1, 0.75)
		else:
			print('Try again')

main()

exit()