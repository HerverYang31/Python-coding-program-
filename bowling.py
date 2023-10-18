bowlingScore = [
  [5,2,0],
  [10,0,0],
  [4,6,0],
  [0,0,0],
  [2,1,0],
  [3,7,0],
  [1,0,0],
  [10,0,0],
  [10,0,0],
  [10,0,0],
  [7,3,0]
]

for row in range(10):
  if bowlingScore[row][0] == 10: #strike
      if bowlingScore[row+1][0] == 10: #two straight strike
        bowlingScore[row][2] = bowlingScore[row][0] + bowlingScore[row+1][0] +bowlingScore[row+2][0]
        print("Frame ",row+1, " is strike")
      else: #one strike 
        bowlingScore[row][2] = bowlingScore[row][0] + bowlingScore[row+1][0] +bowlingScore[row+1][1]
        print("Frame ",row+1," is strike")

  elif bowlingScore[row][0] + bowlingScore[row][1] == 10: #spare
    bowlingScore[row][2] = 10 + bowlingScore[row+1][0]
    print("Frame ",row+1," is spare")

  else: #normal
    bowlingScore[row][2] = bowlingScore[row][0] + bowlingScore[row][1]

total = 0
for row in range(0,11):
  total = total + bowlingScore[row][2]
print("Your final score is ", total)




