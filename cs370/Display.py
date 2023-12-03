from tkinter import *
from tkinter.ttk import *

class Window:
	def __init__(self,window,target,rgb,name,number):
		self.window = window
		self.target = rgbToHex(target[0],target[1],target[2])
		self.hexVal = rgbToHex(rgb[0],rgb[1],rgb[2])
		self.name = name
		self.number = number
		self.draw()

	def draw(self):
		self.canvas = Canvas(self.window)
		self.canvas.create_rectangle(64,64,256,256,outline = "black", fill = self.target, width = 10)
		self.canvas.create_rectangle(448,64,640,256,outline = "black", fill = self.hexVal, width = 10)
		self.canvas.pack(fill = BOTH)
	
def rgbToHex(val1, val2, val3):
	return "#" + hex(val1)[2:] + hex(val2)[2:] + hex(val3)[2:]

def displayColors(target,rgb,name,number):
	tk = Tk() # a tkinter window
	window = Window(tk,target,rgb,name,number)
	tk.title("Closest Paint Color")
	tk.geometry("1080x512")
	mainloop()

def run(target,rgb,name,number):
	displayColors(target,rgb,name,number)

