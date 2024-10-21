user_input = input('choose a function: \n 1: "+" \n 2: "-" \n 3: "*" \n 4: "/" \n')
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
match user_input:
    case "1":
        result = num1 + num2
        print(result)
    case "2":
        result = num1 - num2
        print(result)
    case "3":
        result = num1 * num2
        print(result)
    case "4":
        if (num2 != 0):
            result = num1 / num2
            print(result)
        else: 
            print("Your second number cant be 0: ")
    case "5": 
        print(" You are seccesfuly exit: ")
