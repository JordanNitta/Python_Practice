#The goal of this assignment is for you to use your knowledge of programming concepts and identify them in a new language. 
# write a comment in the same line of the code with the corresponding concept 

num1 = 42 #interger 
num2 = 2.3 #float
boolean = True #Primitive data type which is boolean that means True or False
string = 'Hello World' # String literals enclosed in double quotes 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # A list which is a type of data that is mutable and can hold a group of Values
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # A dictionary which has a group of key value pairs 
fruit = ('blueberry', 'strawberry', 'banana') # A tuple which is immutable(can't be modified after it's created)
print(type(fruit)) # <class 'tuple'>
print(pizza_toppings[1]) # Print 'sausage' since it's index 1
pizza_toppings.append('Mushrooms') # Adds mushrooms to the end of pizza toppings
print(person['name']) # Prints John
person['name'] = 'George' # Changes John to George
person['eye_color'] = 'blue' # Adds eye color as a key to the dict and the value will be blue
print(fruit[2]) # Prints Banana

if num1 > 45:
    print("It's greater") 
else:
    print("It's lower") # Will print its lower 

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") # Will print just right

for x in range(5):
    print(x) #It will print 0, 1, 2, 3, 4 
for x in range(2,5):
    print(x) # It will print 2, 3, 4
for x in range(2,10,3):
    print(x) #It will print 2, 5, 8
x = 0
while(x < 5):
    print(x) # print 0, 1, 2, 3, 4
    x += 1 #incramenting by 1

pizza_toppings.pop() # it will remove mushroom from the list
pizza_toppings.pop(1) # it will remove sausage from the list
print(pizza_toppings)
print(person) # {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color') # Remove key eye color out of the dict
print(person) # {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') # It  will print After 1st statement three times till it stops at olives 
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello') # It will print Hello 10 times

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # Will print hello 4 times 

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4) #prints hello 14 times 


"""
Bonus section
"""

# print(num3)
# num3 = 72
num3 = 72
print(num3)

#fruit[0] = 'cranberry' # won't work since fruit is a tuple

# print(person['favorite_team'])
person['favorite_team'] = 'Lions'
print(person)

#   print(boolean)
print(bool(1))

#fruit.append('raspberry') # won't work since fruit is a tuple

#fruit.pop(1) # won't work since fruit is a tuple


