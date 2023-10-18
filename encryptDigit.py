from array import*

def swap(Darray):
  Darray[0],Darray[2] = Darray[2], Darray[0]
  Darray[1],Darray[3] = Darray[3], Darray[1]

def decrypt(Darray):
  Darray[2],Darray[0] = Darray[0], Darray[2]
  Darray[3],Darray[1] = Darray[1], Darray[3]
  for i in range(0,len(Darray)):
    if Darray[i] - 7 > 0:
      Darray[i] = Darray[i]-7
    else: 
      Darray[i] = Darray[i] + 3
  


digit = int(input("Enter your 4 digit: "))

mDigit = array('i',[0,0,0,0])

for i in range(len(mDigit)-1,-1,-1):
  rem = digit%10
  mDigit[i] = rem
  digit = digit // 10
for i in range(0,4):
  print(mDigit[i], end = " ")
print()

for i in range(len(mDigit)-1,-1,-1):
  mDigit[i]= (mDigit[i]+7)%10


swap(mDigit)

for i in range(0,4):
  print(mDigit[i], end = " ")
print()

decrypt(mDigit)

for i in range(0,4):
  print(mDigit[i], end = " ")
print()





  


  