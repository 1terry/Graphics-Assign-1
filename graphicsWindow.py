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

    '''
    Method drawLine draws a line bewteen two given points in the color of a given color
    We will initialize values depending on four cases, and then run a very similar loop algorithm to the one introduced in class
    There are four cases to consider when drawing a line:
        1. When 0 < slope < 1
        2. When -1 < slope < 0
        3. When slope > 1
        4. When slope < -1
    '''
    def drawLine(self,point1,point2,color): 

        # Gets x and y coordinates of the points and initializes x and y values
        pos1x = point1.get(0,0)
        pos1y= point1.get(1,0)
        pos2x = point2.get(0,0)
        pos2y = point2.get(1,0)
        x = pos1x
        y = pos1y

        # Gets deltas, which are the differences in position of x and y values of the two input points
        deltaY = pos2y - pos1y
        deltaX = pos2x - pos1x  

        # Sets inrement of x and y and draws initial points
        xinc = 1
        yinc = 1
        self.drawPoint([pos1x, pos1y], color)

        # Now we consider the first two cases, for values of the slope between -1 and 1
        if (abs(deltaY) < abs(deltaX)):

            # Case 1: -1 < slope < 0, we will swap the values for this case 
            if (deltaX < 0):
                # We swap the values that the delta calculates
                deltaX = pos1x - pos2x
                deltaY = pos1y - pos2y

                # Swaps x and y 
                temp = pos1x
                pos1x = pos2x
                pos2x = temp
                x = pos1x
                pos1y = pos2y

            # If slope is negative, increment is negative and we will make deltaY positive to update pi
            if deltaY < 0:
                deltaY = -deltaY
                yinc = -1

            # Case 2: When the slope is between 0 and 1, values are initialized by default and will run if the values are not changed in case 1
            while (x < pos2x):
                # If x is the default value, initialize pi
                if (x == pos1x):
                    pi = 2 * deltaY - deltaX
                # Otherwise, update the value of pi depending on if it is positive or negative, increment x and y values and plot the point 
                else:
                    if (pi < 0):
                        pi = pi + 2 * deltaY
                    else:
                        pi = pi + 2 * (deltaY - deltaX)
                        pos1y += yinc
                    pos1x += xinc
                    self.drawPoint([pos1x, pos1y], color)    
                x += 1

        # Otherwise, if slope < -1 or slope > 1, we will consider cases 3 and 4
        else:
            # Case 3: If the slope is negative, we will swap the values we initialized earlier, like in case 1
            if (deltaY < 0):
                deltaX = pos1x - pos2x
                deltaY = pos1y - pos2y
                temp = pos1y
                pos1y = pos2y
                pos2y = temp
                y = pos1y
                pos1x = pos2x

            # Likewise, if deltaX is negative, we will make it positive and change the increment to -1
            if (deltaX < 0):
                xinc = -1
                deltaX = -deltaX
            
            # Case 4 has been initialized previously like case 2, and will initialize automatically if the values are not changed in case 3
            # We also create a loop similar to the previous one, but this time we are iterating through y values and swapping deltaX and deltaY
            while (y < pos2y):
                # Initialize pi if y is at the initial value
                if (y == pos1y):
                    pi = 2 * deltaX - deltaY
                # Otherwise, we update the value of pi depending on if it is negative or positive, increment x and y positions and plot the point
                else:
                    if (pi < 0):
                        pi = pi + 2 * deltaX
                    else:
                        pi = pi + 2 * (deltaX - deltaY)
                        pos1x += xinc
                    pos1y += yinc
                    self.drawPoint([pos1x, pos1y], color)    
                y += 1

    # End of method
       
    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height