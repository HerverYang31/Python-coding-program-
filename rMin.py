def rmin(myArr):
    if len(myArr) == 1:
        return f"The smallest number is {myArr[0]}"
    elif myArr[0] < myArr[1]:
        myArr[1] = myArr[0]
        return rmin(myArr[1:])
    else: 
        return rmin(myArr[1:])

sArr = [1,2,3,4,5,6]
zArr = [2]
hArr = [6,5,4,3,2,1]
print(rmin(sArr))
print(rmin(zArr))
print(rmin(hArr))


a = -121
a = str(a)
print(a[0]==a[1])