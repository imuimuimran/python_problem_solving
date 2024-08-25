# Python program to find the factorial of a number provided by the user.

# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Please enter a positive number")
elif num == 0:
   print("The factorial of", num, "is", factorial)
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
