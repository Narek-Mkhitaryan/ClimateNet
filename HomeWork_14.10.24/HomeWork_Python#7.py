List = []
print (" for exit enter 0: ")
while True:
    enter = str(input("Enter list's items: "))
    if (enter == "0"):
        break
    else:
        List.append(enter)
print(List)
x = len(List)
print(x)
