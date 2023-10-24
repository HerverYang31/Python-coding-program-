class TwoDArr:
    def __init__(self, numRows, numCols):
        self.theRows = [0]*numRows
        for i in range(numRows):
            self.theRows[i] = [0]*numCols
    
    def nRows(self):
        return len(self.theRows)
    
    def nCols(self):
        return len(self.theRows[0])
    
    def getEle(self,row,col):
        return self.theRows[row][col]
    
    def setEle(self,row,col,nValue):
        self.theRows[row][col] = nValue

class Matrix:
    def __init__(self,nRows,nCols):
        self.mat =  TwoDArr(nRows,nCols)
    
    def numRows(self):
        return self.mat.nRows()

    def numCols(self):
        return self.mat.nCols()

    def getItem(self,row,col):
        return self.mat.getEle(row,col)
    
    def setItem(self,row,col,aValue):   
        return self.mat.setEle(row,col,aValue)
    
    def scalar(m1,value):
        row = m1.numRows()
        col = m1.numCols()
        for i in range(row):
            for j in range(col):
                m1.mat.theRows[i][j] = m1.mat.theRows[i][j]*value
        return m1
    
    def transpose(m1):
        row  = m1.numRows()
        col = m1.numCols()
        newM = Matrix(col, row)
        row = newM.numRows()
        col = newM.numCols()
        
        for i in range(row):
            for j in range(col):
                newM.mat.theRows[i][j] = m1.mat.theRows[j][i]
        return newM
    
    def add(m1,m2):
        row = m1.numRows()
        col = m1.numCols()
        m3 = Matrix(row,col)
        for i in range(row):
            for j in range(col):
                m3.mat.theRows[i][j] = m1.mat.theRows[i][j] + m2.mat.theRows[i][j]
        return m3
    
    def subtract(m1,m2):
        row = m1.numRows()
        col = m1.numCols()
        m3 = Matrix(row,col)
        for i in range(row):
            for j in range(col):
                m3.mat.theRows[i][j] = m1.mat.theRows[i][j] - m2.mat.theRows[i][j]
        return m3

sArr = Matrix(3,2)
fArr = Matrix(3,2)

for row in range(3):
    for col in range(2):
        sArr.mat.theRows[row][col]= int(input("Enter your input: "))
for row in range(3):
    for col in range(2):
        fArr.mat.theRows[row][col]= int(input("Enter your input: "))
        
for row in range(3):
    for col in range(2):
        print(sArr.mat.theRows[row][col], end=' ')
    print()
print()
for row in range(3):
    for col in range(2):
        print(fArr.mat.theRows[row][col], end=' ')
    print()
print()    
nArr = Matrix.add(sArr,fArr)
row = nArr.mat.nRows()
col = nArr.mat.nCols()
print('addition of two matrices')
for i in range(row):
    for j in range(col):
        print(nArr.mat.theRows[i][j], end=' ')
    print()

scArr = Matrix.scalar(nArr, 2)
row = scArr.mat.nRows()
col = scArr.mat.nCols()
print('scalar multiplication')
for i in range(row):
    for j in range(col):
        print(scArr.mat.theRows[i][j], end=' ')
    print()
    
tArr = Matrix.transpose(scArr)
row = tArr.mat.nRows()
col = tArr.mat.nCols()
print('transpose')
for i in range(row):
    for j in range(col):
        print(tArr.mat.theRows[i][j], end=' ')
    print()

subArr = Matrix.subtract(sArr,fArr)
row = sArr.mat.nRows()
col = sArr.mat.nCols()
print('Subtract')
for i in range(row):
    for j in range(col):
        print(subArr.mat.theRows[i][j], end = " ")
    print()





