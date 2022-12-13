# import blessed
# from blessed import Terminal
# t = Terminal()

# print(f'{t.link('./ModuleTest#scene2.py', 'scene2')}')

# print('{t.bold}All your {t.red}bold and red base{t.normal}'.format(t=t))
# print(t.wingo(2))



# with t.location(0, t.height - 1):
# 	print('Values')

import calendar
import datetime
from datetime import date
import curses, traceback


def main(stdscr):
	def get_date(datestr, split=False, **kwargs):
		new_date = date.today().strftime(datestr)
		if split != False:
			new_date = new_date.split(split)
		return new_date
	class Pad:
		def __init__(self, x, y, w, h, initfunc=None, **kwargs):
				
			for key in kwargs:
				setattr(self, key, kwargs[key])
				
			self.x = y
			self.y = x
			self.w = h
			self.h = w
			self.pad = curses.newpad(self.w, self.h)
			to_steal = ['box', 'getch', 'addch', 'addstr']
			for i in to_steal:
				setattr(self, i, getattr(self.pad, i))
			"""for key in dir(self.pad):
				if not hasattr(self, key) and key[0] != '_':
					setattr(self, key, getattr(self.pad, key))"""

			if initfunc:
				initfunc(self)
		def moveto(self, x, y):
			self.x, self.y = x, y
			
		def moveby(self, x, y):
			self.x += x
			self.y += y
			
		def redraw(self, copy_x=0, copy_y=0, copy_w=None, copy_h=None, paste_x=None, paste_y=None):
			"""refresh"""
			if copy_w == None:
				copy_w = self.w
			if copy_h == None:
				copy_h = self.h
			if paste_x != None:
				pass# self.moveto(paste_x, paste_y)
			else:
				paste_x, paste_y = self.x, self.y
				
			stdscr.addstr(10, 10, f"{paste_x}, {paste_y}")
			self.pad.refresh(paste_x, paste_y, copy_y, copy_x, copy_w, copy_h)

		# def resize

	#

	# p = Pad(0, 0, 10, 10)
	
	# win = curses.newwin(5, 40, 7, 20)
	
	# pad = curses.newpad(10, 10)
	# for y in range(0, 100):
	# 	for x in range(0, 100):
	# 		try: pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
	# 		except curses.error: pass
	# pad.box()
	# pad.refresh(0, 0, 0, 0, 10, 10)
	# # win.refresh()
	# pad.getch()

	pads = {}
	pads['dummy'] = Pad(0, 0, 1, 1)

	

	def init_calender_pad(self):
		today = get_date('%m/%d/%Y', split='/')
		new_calender_str = str(calendar.month(int(today[2]), int(today[0]))).replace('\n', '\n  ')
		self.addstr(1, 2, new_calender_str)
		self.box()
		self.moveto(5, 5)
		self.redraw()
	pads['calender'] = Pad(0, 0, 24, 9, initfunc=init_calender_pad)

	
	def init_clock_pad(self):
		new_clock_str = str(datetime.datetime.now())
		self.addstr(1, 2, new_clock_str)
		self.box()
		self.redraw(0, 0)
		
	# pads['clock'] = Pad(0, 0, 24, 9, initfunc=init_clock_pad)

	pads['dummy'].getch()
	


def quit():
	stdscr.keypad(0)
	curses.echo()
	curses.nocbreak()
	curses.endwin()
	
if __name__=='__main__':
	try:
		stdscr = curses.initscr()
		curses.noecho()
		curses.cbreak()
		
		stdscr.keypad(1)
		toaddstr = str(dir(stdscr))
		stdscr.addstr(10, 10, toaddstr)
		# stdscr.getch()
		
		(main(stdscr))
		# stdscr.move(curses.LINES - 1, 0)
		# quit()
	except:
		quit()
		traceback.print_exc()
	else:
		curses.endwin()
