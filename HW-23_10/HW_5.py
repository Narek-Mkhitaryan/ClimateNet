list = []

while True:
    a = input("enter list of numbers: ")
    if (a == "exit"):
        break
    else:
        list.append(int(a))
list.sort()
print(list)
print(list[-2])
