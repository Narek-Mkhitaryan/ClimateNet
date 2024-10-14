list = []
while True:
    enter = str(input("Enter your string: "))
    enter = enter.strip()
    if (enter == "exit"):
        break
    else:
        list.append(enter)
x = len(list)
print(x)
print(list)
print("------------------------------------------------------------")
for i in list:
    if list.count(i) > 1:
        while i in list:
            list.remove(i)

print(list)
