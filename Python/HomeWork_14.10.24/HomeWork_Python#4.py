a = str(input("enter a centence: "))
x = "aeiouAEIOU"
count = 0 
for i in a:
    if i in x:
        count += 1
    
print(count)

