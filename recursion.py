def fact(n):
  if n == 0:
    return 1
  else:
    return n*fact(n-1)
  

print(fact(5))

def fibonacci(n):
  if n == 0 or n==1:
    return n
  else:
    return fibonacci(n-1) +fibonacci(n-2)
  
print(fibonacci(1))



def sumOfList(L):
  if len(L) == 1:
    return L[0]
  else:
    return L[0] + sumOfList(L[1:])

    

iList = [2,4,6]
print(sumOfList(iList))
print(iList[2:])