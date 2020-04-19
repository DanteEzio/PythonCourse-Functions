## Factorial number

"""Write a function that receives as parameter one number (must be a integer) and return the factorial of that number.
Example:
```
input -> 5
output -> 120"""

name = input("Input your name: ")
print("welcome", name)

n = int(input("Input your number: "))

def factorial(n):
    if(n==0):
        return 1
    else:
        return n * factorial(n-1)

print("The factorial of your number is: ", factorial(n))


