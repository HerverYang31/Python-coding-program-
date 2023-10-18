from array import*
response = array('i',[1,2,6,4,8,5,9,7,8,10,
                      1,6,3,8,6,10,3,8,2,7,
                      6,5,7,6,8,6,7,5,6,6,
                      5,6,7,5,6,4,8,6,8,10])

sPoll = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}


for i in response:
    sPoll[i]+=1

print(f"{(sPoll)} ")      
    
for i in sPoll:
  print(f"({i}, {sPoll[i]})")
    

