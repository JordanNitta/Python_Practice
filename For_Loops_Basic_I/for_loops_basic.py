#1
#Basic - Print all integers from 0 to 150.
for i in range(0, 151):
    print(i)

#2
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5,1000):
    print(i*5)

#3
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(0,101):
    if i % 5 == 0:
        print("coding", int(i))
    if i % 10 == 0:
        print("Coding Dojo", int(i))

#4
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
min = 0
max = 500000
for number in range(min, max):
    if (number % 2 !=0):
        print(number)

#5
#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

starting_num = 2018
while starting_num > 0:
    starting_num = starting_num - 4
    print(starting_num)

#6
#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and 
#going through highNum, print only the integers that are a multiple of mult. For example, 
#if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1): #It will loop from low num to high num and if its divisiable by 3 it will print the values its divisble by
    if i % mult == 0:
        print(i)
