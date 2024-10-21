a = 0
b = 1
sum = 0
enter = int(input("Enter your number: "))
for i in range( enter):
    sum = a + b 
    a = b
    b = sum 
    print(sum)
