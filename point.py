class Point:
    def __init__(self,x,y):
      self.xValue = x
      self.yValue = y
    def getX(self):
       return self.xValue
    def getY(self):
       return self.yValue
    def shift(self,xInc,yInc):
       self.xValue += xInc
       self.yValue += yInc
    def __repr__(self):
      return f"({self.xValue},{self.yValue})"

pointA = Point(5,7)
pointA.shift(4,2)
pointB = Point(1,1)
pointB.shift(3,4)
print(pointA,pointB, sep=' ')
       