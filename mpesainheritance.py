class Account:
    def __init__(self,account_holder,account_balance):
        self.account_holder=account_holder
        self.account_balance=account_balance
    def deposit(self,amount):
     if amount>0:
      self.account_balance+=amount
      print(f"{amount} deposited successfully.New balance is {self.account_balance}")
     else:
      print("Amount should be greater than zero")
    def withdraw(self,amount):
     if amount>self.account_balance:
       print("Insufficient funds")
     else:
      self.account_balance -=amount
      print(f"{amount} withdrawn successfully.New balance is {self.account_balance}")
    def __str__(self):
       return f"Account holder:{self.account_holder}/nBalance:{self.account_balance}"

class SavingsAccount(Account):
   def __init__(self,account_holder,account_balance,interest_rate):
    super().__init__(account_holder,account_balance)
    self.interest_rate=interest_rate
   def add_interest(self):
    interest=self.account_balance * self.interest_rate/100
    self.account_balance+=interest
    print(f"Interest added successfully.New balance is {self.account_balance}")

   def __str__(self):
    return (f"savings Account holder:" 
            f"{self.account_holder}/nBalance: {self.account_balance},"
            f"interest rate:{self.interest_rate}")
account=Account("Jane",1000)
account.deposit(500)
account.withdraw(200)
print(account)

savings=SavingsAccount('Jane',1000,15)
savings.deposit(400)
savings.withdraw(120)
savings.add_interest()
print(savings)


