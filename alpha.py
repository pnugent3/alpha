""" How quick can you type the alphabet?
"""

import time
import curses

bestTime = 0

def ip(std):
	std.nodelay(1)
	while(1):
		ipVal = std.getch()
		if ipVal < 0:
			continue
		if ipVal == 27:
			return 'abc'
		print(ipVal,end=' ')
	

def main():
	print("Time how quickly you can type the alphabet A->Z")
	print("(Either lower case or upper, it doesn't matter)")
	print("The time will begin when you press A and end when you press Z")
	print("Press ESC to abort")

	
	ipc=curses.wrapper(ip)
	

	print(ipc)
	



if __name__ == "__main__":
	main()