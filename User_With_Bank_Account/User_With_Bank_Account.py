class BankAccount:

    Total_Balance = []
    # don't forget to add some default values for these parameters!
    def __init__(self, first_name, last_name, int_rate, balance=0): # This is a constructor method that gets called when an instance of the class is made.
        self.first_name = first_name
        self.last_name = last_name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.Total_Balance.append(self) # This will add the instances to the Total_Balance Variable

# deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount): #This method will add  the account balance by the given amount
        self.balance += amount
        return self

# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds;
# if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount): # This method will decrease the balance by the amount if there is sufficient funds if not it will print(Insufficient funds: Charging a $5 fee")
        if self.balance > amount:
            self.balance -= amount
            print(f"{self.first_name} {self.last_name}: Withdrawn ${amount}. Available balance: ${self.balance}")
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
            print(f"User: {user_account.first_name} {user_account.last_name}, Interest rate: {user_account.int_rate} Balance: ${user_account.balance}")
        return user_account

# user_jordan = BankAccount("Jordan Bill", 0.2) #This line creates a new instance of BankAccount and adds it to a Object user_jordan. Jordan Bill is added to name attribute, 0.2 is added to int_rate attribute.
# #print(user_jordan.name) You can access the attributes and methods by calling on the instance
# user_jordan.deposit(1000).withdraw(200).yield_interest().display_account_info()
# BankAccount.display_balance() # This will store all the instances of the class in a list
# print("=========================================================================")
# user_Bob = BankAccount("Bob Chub", 0.5, 0) 
# user_Bob.deposit(3000).withdraw(200).yield_interest().display_account_info()

# BankAccount.display_balance() # This will store all the instances of the class in a list

class User: 
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.checking = BankAccount(self.first_name, self.last_name, 0.1, 0) #instance of the bank account class.
        self.saving = BankAccount(self.first_name, self.last_name, 0.2, 0)

    # Making a deposit to checking or savings using the deposit method defined in the bankaccount class
    def make_deposit(self, amount, account):
        if account == "checking":
            self.checking.deposit(amount) 
            print(f"{self.first_name} {self.last_name}: Checking Balance is now: ${self.checking.balance}")
        elif account == "saving":
            self.saving.deposit(amount)
            print(f"{self.first_name} {self.last_name}: Savings Balance is now: ${self.saving.balance}")
        return self

    # Making a withdraw from checking or savings using the withdraw method defined in the bankaccount class
    def make_withdraw(self, amount, account):
        if account == "checking":
            self.checking.withdraw(amount)
            print(f"{self.first_name} {self.last_name}: Withdrawn ${amount} dollars from Checking Balance now is: {amount}")
        elif account == "saving":
            self.saving.withdraw(amount)
            print(f"{self.first_name} {self.last_name}: Withdrawn ${amount} dollars from saving Balance now is: {amount}")
        return self

    #This allow are users to be able to transfer money to each other with adding person into the parameter
    def transfer_money(self, amount, person, account):
        if account == "checking":
            if self.checking.balance < amount:
                print("Insuffient Funds:")
                return self
            else: 
                self.checking.withdraw(amount)
                person.checking.deposit(amount)
                print(f"Transfering: ${amount} from {self.first_name} {self.last_name} Checking Account To: {person.first_name} {person.last_name} Checking Account")
                return self
        elif account == "saving":
            if self.saving.balance < amount:
                print("Insufficient Funds")
                return self
            else:
                self.saving.withdraw(amount)
                person.saving.deposit(amount)
                print(f"Transfering: ${amount} from {self.first_name} {self.last_name} Saving Account To: {person.first_name} {person.last_name} Saving Account")
                return self

    def display_user_balance(self):
        print(f"User: {self.first_name} {self.last_name} Checking: ${self.checking.balance}")
        print(f"User: {self.first_name} {self.last_name} Saving: ${self.saving.balance}")
        return self

user_1 = User("Jimmy", "Bill", "b@email.com")
user_1.checking.display_balance() #This line wont say if its in checking or saving will just display balance
user_1.saving.display_balance() #This line wont say if its in checking or saving will just display balance

user_1.make_deposit(1000, "checking")
user_1.make_deposit(5000, "saving")
user_1.make_withdraw(100, "checking")
user_1.make_withdraw(2000, "saving")
user_1.display_user_balance()

jordan = User("Jordan", "Bob", "b@email.com")
jordan.checking.display_balance()
jordan.saving.display_balance()
# user_jimmy.BankAccount()
jordan.make_deposit(1000, "checking")
jordan.make_deposit(5000, "saving")
jordan.make_withdraw(100, "checking")
jordan.make_withdraw(2000, "saving")
jordan.transfer_money(200, user_1, "checking")
user_1.transfer_money(200, jordan, "checking")
jordan.display_user_balance()