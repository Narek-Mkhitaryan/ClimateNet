list = []
print("Enter 3 numbers: ")
a,b,c = [int(input(f'Enter noumber {i}: ')) for i in ['a', 'b', 'c']] 
for i in [a,b,c]:
    list.append(i)
print(max(list))
