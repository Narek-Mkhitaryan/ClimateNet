while True:
    enter_num = int(input("Enter a number: "))
    if (enter_num > 0):
         match enter_num % 2:
            case 0:
                print(f"{enter_num} is an even number: ")
            case 1:
                print(f"{enter_num} is an odd number: ")
    elif(enter_num == 0):
        print("You are exit: ")
        break
    else:
        print("There is an error in the given number: ")
       
    
