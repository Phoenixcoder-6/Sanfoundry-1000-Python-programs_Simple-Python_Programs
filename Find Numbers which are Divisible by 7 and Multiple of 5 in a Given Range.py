''' This is a Python Program to find those numbers which are divisible by 7 and multiple of 5 in a given range of numbers.

Problem Description
The program takes an upper range and lower range and finds those numbers within the range which are divisible by 7 and multiple of 5.

Problem Solution
1. Take in the upper and lower range and store it in separate variables.
2. Use a for loop which ranges from the lower range to the upper range.
3. Then find the numbers which are divisible by both 5 and 7.
4. Print those numbers
5. Exit.'''

#SOURCE CODE

U=int(input("Enter the upper range:"))
L=int(input("Enter the lower range:"))

for i in range(L,U+1):
    if(i%7==0  and i%5 == 0):
        print(i)
