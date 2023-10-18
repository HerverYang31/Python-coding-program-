class Matrix:
    def __init__(self,nRows,nCols):
        self.theRow = [0]*nRows
        for i in range(nRows):
            self.theRow[i] = [0]*nCols
    
    def numRows(self):
        return f"Numbe of the rows: {len(self.theRow)}"

    def numCols(self):
        return f"Number of the columns: {len(self.theRow[0])}"

    def getItem(self,row,col):
        return f"The item is {self.theRow[row][col]}"
    
    def setItem(self,row,col,nValue):
        self.theRow[row][col] = nValue
    
    def scalar(self,value):
        for row in range(len(self.theRow)):
            for col in range(len(self.theRow[0])):
                self.theRow[row][col] = (self.theRow[row][col])*value
    
    def transpose(self):
        for row in range(len(self.theRow)):
            for col in range(len(self.theRow[0])):
                self.theRow[col][row] = self.theRow[row][col]


def add(aMatrix,bMatrix):
    for row in range(len(aMatrix)):
        for col in range(len(aMatrix[0])):
            aMatrix[row][col] = aMatrix[row][col] + bMatrix[row][col]
    return aMatrix


sArr = Matrix(2,3)

for row in range(2):
    for col in range(3):
        sArr.theRow[row][col] = int(input("Enter your number: "))

print()
print(sArr.numRows())
print(sArr.numCols())
print(sArr.getItem(0,0))
sArr.scalar(3)
print()
print("Scalar Multiplication")
for row in range(len(sArr.theRow)):
    print(sArr.theRow[row])

print()
print("Transpose")
sArr.transpose()
for row in range(len(sArr.theRow)):
    print(sArr.theRow[row])

matrix1 = [[11,22,33,44],
           [55,66,77,88],
           [99,111,222,333],
           [444,555,666,777]]
matrix2 = [[777,666,555,444],
           [333,222,111,99],
           [88,77,66,55],
           [44,33,22,11]]

matrix1.add(matrix1,matrix2)
for row in range(len(matrix1)):
    print(matrix1[row])

