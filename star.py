size = 3
while size <=7: 
  for row in range(0,size):
    for col in range(0,size):
      if row==col or col == size-1-row:
        print("*", end = " ")
      else:
        print(" ", end = " ")      
    print()
  size+=2
  



