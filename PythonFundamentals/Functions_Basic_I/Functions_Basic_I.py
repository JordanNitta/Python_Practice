#For each of the following code snippets, first predict the output (what you will see printed to the terminal). 
# Once you've made a prediction, run the code snippet to see if you are correct!

#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) 
#Answer - It will just return the interger value which is 5 when we call the function

#2

def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#Answer - Its going to give an error because were calling a function which is number_of_days_in_a_week_silicon_or_triangle_sides() that does not exist. 

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#Answer - It will return 5 because the return statement cause the function to exit. The second statment will never be executed

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Answer - It will return 5 and then exit out of the function and the print statement will not be executed

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Answer - It will print 5 and none since there is no return statement
'''
#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Answer - It will print 3 and 5 which is the sum of the arguments were passing in. If you add a return statment on the second line it will return the values added together.
'''
#7
def concatenate(b,c):
    return str(b)+str(c)
    print(concatenate(2,5))
#Answer - It will return none since the print statement is after the reuturn

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#Answer - It will print a 100 then it would go to the else statement and return 10 and exit out of the function since the return 7 is at the end.

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Answer - The first print statement will return 7. The second print statement will return 14. The third statement at the first argument will return 7 and the second argument will reutrn 14. Then you will have to add 14 + 7 = 21 and the result will print 21 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Answer - Will return 8 because it's adding the two arguments that's getting passed in the function. Won't return 10 because it's is after the first return statement

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#Answer - The first line will print 500. When the function starts it will print 300, 300. The last line will print 500 since its taking the variable thats outside of the function.

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#Answer - The first line will print 500. When the fucntion starts it will print 300. The last line will print 500.

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#Answer - The first line will print 500. When the function starts it will print 300. The last line will print 500.

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#Answer -  Will print 1, then 3 because function bar() is called before the second print statement then it will execute and print 2. Result would be 1, 3, 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#Answer - Will print 1, 