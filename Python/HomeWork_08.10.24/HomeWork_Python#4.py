import random 

random_num = random.randint(1, 10)
print (random_num)
while True:
    enter =int(input("Enter a number 1-10: "))
    if (enter > 0 and enter < 11):
    
        if (enter == random_num):
            print("you gest the number")
            break
        elif(enter > random_num):
            print("input a smaller number: ")
        else:
            print("input a higher number: ")
    else: 
        print("type in given diapason: ")

