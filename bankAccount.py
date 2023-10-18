class BankAccount:
    def __init__(self,a_owner,a_type,a_balance):
      self.owner = a_owner
      self.type = a_type
      self.balance = a_balance
    
    def deposite(self, d_money):
       self.balance = self.balance + d_money
    
    def withdraw(self, w_money):
       self.balance = self.balance - w_money
    
    def check(self):
       return self.balance
    
    def __repr__(self):
       return f"Name: {self.owner},Type: {self.type}, Balance: {self.balance}"

yang = BankAccount("Yang","Saving",1000)

b = yang.check()
print(b)