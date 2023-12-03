import csv
import math

class PaintSelector:
    paints = list()
    filename = ""
    target = tuple()
    r0 = None
    g0 = None
    b0 = None

    def __init__(self):
        return

    def setTarget(self, color):
        self.target = color
        return
    
    def setFilename(self,filename):
        self.filename = filename

    def _hexToDecimal(self,hex):
        return int(hex,16)

    def _extractColors(self,rgb):
        red = self._hexToDecimal(rgb[0:2])
        green = self._hexToDecimal(rgb[2:4])
        blue = self._hexToDecimal(rgb[4:])
        return (red,green,blue)

    #csv is in format: name,number,hex,rgb
    def _readCSV(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row[2] = self._extractColors(row[2])
                row = row[:3]
                self.paints.append(row)

    def _distance(self,color):
        r1 = color[0]
        g1 = color[1]
        b1 = color[2]
        return math.sqrt((r1-self.r0)**2 + (g1-self.g0)**2 + (b1-self.b0)**2)

    def _findClosestColor(self):
        self.r0 = self.target[0]
        self.g0 = self.target[1]
        self.b0 = self.target[2]
        best = self.paints[0]
        bestDistance = self._distance(self.paints[0][2])
        currDistance = 0
        for paint in self.paints:
            currDistance = self._distance(paint[2])
            if currDistance < bestDistance:
                bestDistance = currDistance
                best = paint
        return best

    def run(self):
        self._readCSV()
        return self._findClosestColor()
