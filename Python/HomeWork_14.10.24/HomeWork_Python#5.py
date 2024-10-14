number = 0 
given = int(input("Enter a number: "))
given = str(given)
x = len(given)

for i in range(x):
   number += int(given[i])
print(f'sum of elements {number}')
