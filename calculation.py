class calculation:
    def __init__(self, *inData):
        if len(inData) == 2:
            self.result == self.sub(inData)
        elif len(inData) == 4:
            self.result = self.add(inData)
        else:
            self.result = self.mul(inData)
    
    def add(self,args):
        sum = 0
        for i in range(len(args)):
            sum += args[i]
        return sum
    def sub(self,args):
        return args[0] - args[1]
    def mul(self, args):
        total = 1
        for i in range(len(args)):
            total *= args[i]
        return total

obj1 = calculation(1,2,3,4)
obj2 = calculation(10,20)
obj3 = calculation(1,2,3,4,5)
print(obj1.result," ",obj2.result," ",obj3.result)