a ,b = [int(input(f'enter a number {i}; ')) for i in ['a', 'b']]
list = [] 
if(a >= b and a != 0 and b != 0): 
    for i in range (1, a+1):
        for j in range(1, b+1):
            if(a % i == 0 and b % j ==0 and i == j):
                list.append(i)
elif(a < b and a != 0 and b != 0):  
    for i in range (1, b+1):
        for j in range(1, a+1):
            if(b % i == 0 and a % j ==0 and i == j):
                list.append(i)
print(list)
print(max(list))



# une solution alternative
#improt math

#math.gcd(a,b)
