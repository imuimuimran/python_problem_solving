# Write a program to print fibonacci series upto n terms in python

num = int(input("Enter the number of terms: "))

if num <= 0:
    print("Please enter a positive integer.")
elif num == 1:
    print("Fibonacci Series: 0")
else:
    n1, n2 = 0, 1
    print("Fibonacci Series:", n1, end=", ")
    if num > 1:
        print(n2, end=", ")
    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if i == num - 1:
            print(n3)  # Last term without a comma
        else:
            print(n3, end=", ")  # Terms with commas
