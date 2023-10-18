def hanoiTower(nDisks, From, To):
  if nDisks == 1:
    return str(From) + "-->" + str(To) + "\n" 
  else: 
    temp = 6 - From - To
    return hanoiTower(nDisks - 1, From, temp) + str(From) + "-->" + str(To) + "\n" + hanoiTower(nDisks - 1, temp, To)


output = hanoiTower(3, 1, 3)
print(output)
