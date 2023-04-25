''' This is a Python Program to print odd numbers within a given range.

Problem Description
The program takes the upper and lower limit and prints all odd numbers within a given range.

Problem Solution
1. Take in the upper range limit and the lower range limit and store it in separate variables.
2. Use a for-loop ranging from the lower range to the upper range limit.
3. Then use an if statement if check whether the number is odd or not and print the number.
4. Exit.'''

#Source Code

a=int(input("Enter the range:"))
print("The odd numbers are:") 

for i in range(0,a+1):
    if(i%2 !=0):
        print(i)
else:
    pass
