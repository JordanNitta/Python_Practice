class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("------------------------")
        # print(f"""
        # {self.first_name},
        # {self.first_name}, 
        # {self.email}, 
        # {self.age}, 
        # {self.is_rewards_member}, 
        # {self.gold_card_points}""")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        if self.is_rewards_member:
            print("User already a member.")
        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You dont have enough points.")
            return self
        self.gold_card_points -= amount
        return self
    
user_1 = User("Jordan", "Bob", "JB@email.com", 22)
user_1.display_info().enroll().spend_points(50).display_info()
'''
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(200)
my_user.display_info()
'''

my_user2 = User("Bob", "R", "J@", 40)
my_user2.display_info()
my_user2.enroll()
my_user2.spend_points(80)


