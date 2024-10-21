a = 0
while True:
    print("Enter 1 for continue: ")
    print("Enter 2 for exit: ")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        number = int(input("Enter your number: "))
        a = a + number
    elif(choice == 2):
        print(a)
        break
    else:
        print("your choice is wrong: ")
