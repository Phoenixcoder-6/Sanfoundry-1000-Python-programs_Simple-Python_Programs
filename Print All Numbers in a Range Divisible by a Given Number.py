''' This is a Python Program to print all numbers in a range divisible by a given number.

Problem Description
The program prints all numbers in a range divisible by a given number.

Problem Solution
1. Take in the upper range and lower range limit from the user.
2. Take in the number to be divided by from the user.
3. Using a for loop, print all the factors which is divisible by the number.
4. Exit. '''

#SOURCE CODE:

Up=int(input("Enter the upper range:"))
Low=int(input("Enter the lower range:"))
n= int(input("Enter the given number:"))

for i in range(Low,Up+1):
    if(i%n ==0):
        print(i)
