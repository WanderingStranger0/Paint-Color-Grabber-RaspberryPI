import os, time
import ProcessImage
import Display as dy
from PaintSelector import PaintSelector

os.system("libcamera-jpeg -o rawimage.jpg") #takes a picture
os.system("clear")
target = ProcessImage.run()
ps = PaintSelector()
ps.setTarget(target)
ps.setFilename("/home/derrick/cs370/paints.csv")
myPaint = ps.run()
print("TARGET: ",target)
print("PAINT: ", myPaint)
dy.run(target,myPaint[2],myPaint[1],myPaint[0]) # target, rbg, name, number
