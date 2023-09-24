from balance_accounts import *

Noman = BankAccount("Noman",2000)
Sara = BankAccount("Sara",2500)

Noman.getBalance()
Sara.getBalance()

Sara.deposit(2000)

Noman.withDraw(10)

Noman.transfer(10000,Sara)
Noman.transfer(100,Sara)

Jim = InterestRewards("Jim",1000)

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(200,Noman)


Blaze = SavingAcc("Blaze",1000)

Blaze.deposit(100)

Blaze.transfer(10000,Sara)
Blaze.transfer(1000,Sara)