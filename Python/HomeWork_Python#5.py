def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))
if (number >= 0):
    result = factorial(number)
    print(result)
else:
    print("there is an mistake: ")

