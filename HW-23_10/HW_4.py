a = int(input("enter anumber: "))
count = 0
b = len(str(a))
for i in str(a):
    count += int(i) ** b
if( count == a ):
    print("Your number is an Armstrong number: ")
else:
    print("Your number isn't an Amstrong number: ")
