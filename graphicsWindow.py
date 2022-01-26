import operator
from PIL import Image
from matrix import matrix

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self,point,color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0],point[1]] = color

    '''Function'''
    def drawLine(self,point1,point2,color): 
        pos1x = point1.get(1,1)
        pos1y= point1.get(2,1)
        x = pos1x
        y = pos1y
        pos2x = point2.get(1,1)
        pos2y = point2.get(2,1)
        deltaY = pos2y - pos1y
        deltaX = pos2x - pos1x  

        p1 = 0 
        yi = 1  

        # Delta x is diff between x max and x min
        # Delta y is diff between y max and y min

        # If slope is negative
        if deltaY < 0:
            deltaY = -deltaY
            yi = -1

        # if deltaX < 0:


        # For slopes ranging from 0 - 1
        while (x != pos2x):
            if (x == pos1x):
                p1 = 2 * deltaY - deltaX
            else:
                if (p1 < 0):
                    p1 = p1 + 2 * deltaY
                else:
                    p1 = p1 + 2 * (deltaY - deltaX)
                    y = y + yi
                x = x + 1
                self.drawPoint(x, y)



        print(point1)
        print(point2)

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height