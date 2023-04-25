''' Problem Description
The program prints all integers that aren’t divisible by either 2 or 3 and lies between 1 and 50.

Problem Solution
1. Use a for-loop ranging from 0 to 51.
2. Then use an if statement to check if the number isn’t divisible by both 2 and 3.
3. Print the numbers satisfying the condition.
4. Exit.''' 
#SOURCE CODE: 

for i in range(1,51): 
    if i%2==0: 
        continue 
    if i%3==0: 
        continue 
    else: 
        print(i) 
