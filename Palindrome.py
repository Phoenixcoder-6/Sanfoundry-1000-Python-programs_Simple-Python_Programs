''' This is a Python Program to check whether a given number is a palindrome.

Problem Description
The program takes a number and checks whether it is a palindrome or not.

Problem Solution
1. Take the value of the integer and store in a variable.
2. Transfer the value of the integer into another temporary variable.
3. Using a while loop, get each digit of the number and store the reversed number in another variable.
4. Check if the reverse of the number is equal to the one in the temporary variable.
5. Print the final result.
6. Exit. '''

#SOURCE CODE:

a=int(input("Enter any number to check:"))
temp = a
rev=0
while(a>0):
    dig = a%10
    rev = rev*10 + dig
    a= a//10
if(temp == rev):
    print ("Palindrome!")
else:
    print("Not palindrome!!")
