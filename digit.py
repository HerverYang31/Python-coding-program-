from array import*
num = int(input("Enter your number: "))

myArray = array('i',[0,0,0,0,0])
for i in range(len(myArray)-1,-1,-1):
  rem = num%10
  myArray[i] = rem
  num = num // 10

for i in range(0,5):
  print(myArray[i], end = "   ")


