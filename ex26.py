class bankAccount:
    balance=0
    
    def __init__(self, balance):
        self.balance=balance
        
    def deposit(self, amount):
        print(f"Your balance is {self.balance + amount}")
    def withdraw(self, amount):
        print(f"Your balance is {self.balance - amount}")
        

ba1=bankAccount(100)
ba1.deposit(50)
ba1.withdraw(50)
