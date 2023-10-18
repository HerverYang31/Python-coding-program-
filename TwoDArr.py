class TwoDArr:
    def __init__(self, numRows, numCols):
        self.theRows = [0]*numRows
        for i in range(numRows):
            self.theRows[i] = [0]*numCols
    
    
    def nRows(self):
        return f"Number of rows: {len(self.theRows)}"
    
    def nCols(self):
        return f"Number of columns: {len(self.theRows[0])}"
    
    def getEle(self,row,col):
        return f"Element is {self.theRows[row][col]}"
    
    def setEle(self,row,col,nValue):
        self.theRows[row][col] = nValue



sArr = TwoDArr(3,2)

for row in range(3):
    for col in range(2):
        a= int(input("Enter your input: "))
        sArr.theRows[row][col]= a

print(sArr.nRows())
print(sArr.nCols())
print(sArr.getEle(0,1))
sArr.setEle(0,1,5)

for row in range(3):
    for col in range(2):
        print(sArr.theRows[row][col], end = " ")
    print()




