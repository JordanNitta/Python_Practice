class BankAccount:

    Total_Balance = []
    # don't forget to add some default values for these parameters!
    def __init__(self, name, int_rate, balance=0): # This is a constructor method that gets called when an instance of the class is made.
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        self.Total_Balance.append(self) # This will add the instances to the Total_Balance Variable

# deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount): #This method will add  the account balance by the given amount
        self.balance += amount
        return self

# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds;
# if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount): # This method will decrease the balance by the amount if there is sufficient funds if not it will print(Insufficient funds: Charging a $5 fee")
        if self.balance > amount:
            self.balance -= amount
            print(f"{self.name}, Withdrew ${amount}. Available balance: ${self.balance}")
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self): #This method will make the account balance go up by mulitplying the current balance and whatever interest rate is given.
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            print(f"Balance After Yield Interest: {self.balance}")
        return self
        
    def display_account_info(self):
        # print(f"User Bank Account Info: {self.name} Available Balance: {self.balance} ")
        return self
    
    
    @classmethod
    def display_balance(cls):  #This class method iterates through the variable Total_Balance and prints the account name, interest rate, and balance. It also has the instance attributes name, int_rate, balance.
        print("Account Info:")
        for user_account in cls.Total_Balance:
            print(f"User: {user_account.name}, Interest rate: {user_account.int_rate} Balance: ${user_account.balance}")
        return user_account

user_jordan = BankAccount("Jordan Bill", 0.2) #This line creates a new instance of BankAccount and adds it to a Object user_jordan. Jordan Bill is added to name attribute, 0.2 is added to int_rate attribute.
#print(user_jordan.name) You can access the attributes and methods by calling on the instance
user_jordan.deposit(1000).withdraw(200).yield_interest().display_account_info()
BankAccount.display_balance() # This will store all the instances of the class in a list
print("=========================================================================")
user_Bob = BankAccount("Bob Chub", 0.5, 0) 
user_Bob.deposit(3000).withdraw(200).yield_interest().display_account_info()

BankAccount.display_balance() # This will store all the instances of the class in a list


