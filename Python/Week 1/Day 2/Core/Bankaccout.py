class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts=[]
    bank_name = "BSBank"
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
               # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        return self
        # your code here
    def withdraw(self, amount):
        # your code here
        if amount>self.balance:
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance-=amount
        return self 
    def display_account_info(self):
        # your code here
        print("balance: ", self.balance)
        return self 
    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        # your code here
        return self 
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
        print(cls)
    

my_new_bank = BankAccount.change_bank_name("Amen Bank")
# my_new_bank = BankAccount.bank_name()
print(my_new_bank)
nawfel=BankAccount(2,1000)
iheb=BankAccount(1,1500)

nawfel.deposit(2000).deposit(500).deposit(3000).withdraw(3000).yield_interest().display_account_info()
iheb.deposit(3000).deposit(1000).withdraw(200).withdraw(1000).withdraw(300).withdraw(1000).yield_interest().display_account_info()

# nawfel.all_balances()