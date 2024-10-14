print("Enter exit for exit :) ")
count = 0
while True:
    enter = input("Enter a number: ")
    if(enter == "exit"):
        break    
    else:
        count += int(enter)
print(count)
