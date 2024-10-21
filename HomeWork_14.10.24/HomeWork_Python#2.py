def  prime (n):
    if n <= 1:
        return "Not Prime"
    for i in range(2,int(n//2)+1):
        if n % i ==0:
            return "Not Prime"
    return "Prime"
n = int(input("Enter a number: "))
print(prime(n))
