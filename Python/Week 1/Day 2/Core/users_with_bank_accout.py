class BankAccount:
    
    all_accounts=[]
    bank_name = "BSBank"
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
        
    def deposit(self, amount):
        self.balance+=amount
        return self
        
    def withdraw(self, amount):
        
        if amount>self.balance:
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance-=amount
        return self 
    def display_account_info(self):
        
        print("balance: ", self.balance)
        return self 
    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        
        return self 
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.deposit(amount))
        return self
    	# your code here

    
    
nawfel=BankAccount(2,1000)
iheb=BankAccount(1,1500)
aziz=User("aziz","gfj@")
nawfel.deposit(2000).deposit(500).deposit(3000).withdraw(3000).yield_interest().display_account_info()
iheb.deposit(3000).deposit(1000).withdraw(200).withdraw(1000).withdraw(300).withdraw(1000).yield_interest().display_account_info()
aziz.make_deposit(200)

