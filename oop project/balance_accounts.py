class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,accountName,accountBalance):
        self.name = accountName
        self.balance = accountBalance
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def getBalance(self):
        print(f"Account : '{self.name}'. Balance : ${self.balance:.2f}.")
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDeposit Completed!!\n")
        self.getBalance()
        
    def viableTransactions(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry {self.name} , You have only {self.balance:.2f} Balance only."
            )

    def withDraw(self,amount):
        try:
            self.viableTransactions(amount)
            self.balance = self.balance - amount
            print("\nWithdraw completed!! \n")
            self.getBalance()
        except BalanceException as error:
                print(f"\n Error Interrupted:{error}")
                
    def transfer(self,amount,account):
        try:
            print(f"\n***********Balance Transfer Started!! 🚀 ***********")
            self.viableTransactions(amount)
            self.withDraw(amount)
            account.deposit(amount)
            print(f"\n***********Transfer Completed 🎉***********")
        except BalanceException as error :
            print(f"Transfer Interrupted ❌ {error}")
    
    
class InterestRewards(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()
    
class SavingAcc(InterestRewards):
    def __init__(self, accountName, accountBalance):
        super().__init__(accountName, accountBalance)
        self.fee = 5
        
    def withDraw(self,amount):
        try:
            self.viableTransactions(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f"\nWithDraw Completed")
            self.getBalance()
        except BalanceException as error:
            print(f'Error Interrupted!!{error}')
                    
        