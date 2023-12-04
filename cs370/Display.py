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
		targetColorText = str(self.target)
		paintColorText = str(self.hexVal)
		paintNameText = self.name + " " + self.number

		self.canvas.create_rectangle(64,64,256,256,outline = "black", fill = self.target, width = 10)
		self.canvas.create_text(164, 30, text="Wall Color", fill="black", font=('Helvetica 15 bold'))
		self.canvas.create_rectangle(448,64,640,256,outline = "black", fill = self.hexVal, width = 10)
		self.canvas.create_text(544, 30, text=paintNameText, fill="black", font=('Helvetica 15 bold'))
		self.canvas.create_text(164, 50, text=str(targetColorText), fill="black", font=('Helvetica 15 bold'))
		self.canvas.create_text(544, 50, text=str(paintColorText), fill="black", font=('Helvetica 15 bold'))
		self.canvas.pack(fill = BOTH)
	
def rgbToHex(val1, val2, val3):
    return '#%02x%02x%02x' % (val1, val2, val3)

def displayColors(target,rgb,name,number):
	tk = Tk() # a tkinter window
	tk.geometry("700x500")
	window = Window(tk,target,rgb,name,number)
	tk.title("Closest Paint Color")
	
	mainloop()

def run(target,rgb,name,number):
	displayColors(target,rgb,name,number)

