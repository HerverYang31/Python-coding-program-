from array import*  
class dailyTemp:
  def __init__(self, tarry):
    self.TemArray = tarry

  def printArr(self):
    for i in range(0,len(self.TemArray)):
      print(self.TemArray[i], end = " ")

  def freezing(self):
    count = 0
    for i in range(0,len(self.TemArray)):
      if self.TemArray[i] < 32:
        count+=1
    return f"No of Temperature below 32: {count}"

  def lowest(self):
    low = min(self.TemArray)
    return f"Lowest Temperature: {low}"

  def bubSortDesc(self):
    loops = 1
    while loops < len(self.TemArray):
      for i in range(0,len(self.TemArray)-loops):
        if self.TemArray[i] < self.TemArray[i+1]:
          self.TemArray[i], self.TemArray[i+1] = self.TemArray[i+1], self.TemArray[i]
      loops+=1
    for ele in self.TemArray:
      print(ele, end = " ")

  

temp = dailyTemp(array('f',[34.0,23.0,15.0,50.0,60.0,70.0,90.0]))
temp.printArr()
print()
print(temp.freezing())
print(temp.lowest())
temp.bubSortDesc()





