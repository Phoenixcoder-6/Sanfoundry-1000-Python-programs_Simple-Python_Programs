''' This is a Python Program to find the sum of digits in a number.

Problem Description
The program takes in a number and finds the sum of digits in a number.

Problem Solution
1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and add the digits to a variable.
3. Print the sum of the digits of the number.
4. Exit. '''

#SOURCE CODE:

p=int(input("Enter any digit:"))
sum=0

while(p>0):
    dig=p%10
    sum=sum+dig
    p=p//10
print("The sum of digis are:", sum)
