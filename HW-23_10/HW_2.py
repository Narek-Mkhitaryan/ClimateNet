enter = str(input("Enter your string: "))
vowel = "aeuio"
enter = enter.lower()
count = 0
for i in enter:
   if i in vowel:
       count += 1
print(f'In your string there is {count} vowel: ')
