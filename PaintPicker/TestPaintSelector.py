from PaintSelector import PaintSelector

myWall = "808080"
file = "src\\fakeColors.csv"

ps = PaintSelector()
ps.setTarget(myWall)
ps.setFilename(file)
myPaint = ps.run()

#Test should return grey
print("TESTING:  closest paint to", myWall)
print("RETURNED:", myPaint)
