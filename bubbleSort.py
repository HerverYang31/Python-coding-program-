from array import*
myArray = array("i",[29,10,14,37,13])
loops = 1
while loops < len(myArray):
  for i in range(0,len(myArray)-loops):
    if myArray[i] > myArray[i+1]:
      temp = myArray[i]
      myArray[i] = myArray[i+1]
      myArray[i+1]= temp
  loops+=1
for ele in range(0,len(myArray)):
  print(myArray[ele], end = " ")

print()
a = "hello, world: hey"
left = 0
b = not a[left].isalnum()
c = a[left].isalnum()
print(b,c)