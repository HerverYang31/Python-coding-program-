class Student:
    def __init__(self,sName,sMajor,sTaking_python):
      self.name = sName
      self.major = sMajor
      self.taking_python = sTaking_python
    
    def study(self):
       print("I am studying Python")

    def __repr__(self): ##dont have to print each of them for calling each attribute
      return f"student's name = {self.name}, student's major = {self.major}, student's Python class = {self.taking_python}"

john = Student("John Smith","Computer Science",True)
print(john)
john.study()
