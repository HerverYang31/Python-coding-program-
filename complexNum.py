class Complex:
    def __init__(self,r,i):
      self.rPart = r
      self.iPart = i
    def add(a,b):
       rN = a.rPart+b.rPart
       iN = a.iPart + b.iPart
       return complex(rN,iN)
    def subtract(a,b):
       rN = a.rPart - b.rPart
       iN = a.iPart - b.iPart
       return complex(rN,iN)
    def multiply(a,b):
       rN = (a.rPart * b.rPart) + (a.iPart * b.iPart*-1)
       iN = (a.rPart * b.iPart) + (a.iPart * b.rPart)
       return complex(rN,iN)     
    def __repr__(self):
        return f"{self.rPart,self.iPart}"
    
a = Complex(2,-5)
b = Complex(2,4)
c = Complex.add(a,b)
d = Complex.subtract(a,b)
e = Complex.multiply(a,b)

print(a)
print(b)
print(c)
print(d)
print(e)
