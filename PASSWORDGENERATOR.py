import random
lower_letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','m','n','o','p','q','r','s','t','u','w','x','y','z']
upper_letters =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','&','*','+']
print("WELCOME TO THE PASSWORD GENERATOR")
n_upper_letters=int(input("HOW MANY UPPER LETTERS YOU WANT IN YOUR PASSWORD?\n"))
n_lower_letters=int(input("HOW MANY LOWER LETTERS YOU WANT IN YOUR PASSWORD?\n"))
n_numbers=int(input("HOW MANY NUMBERS YOU WANT IN YOUR PASSWORD?\n"))
n_symbols=int(input("HOW MANY SYMBOLS YOU WANT IN YOUR PASSWORD?\n"))
password=" "
for i in range(1,n_upper_letters-1):
    char = random.choice(upper_letters)
    password = password+char
    password += char

for i in range(1,n_lower_letters-1):
    char = random.choice(lower_letters)
    password = password+char
    password += char

for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password += char
for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password = password+char
    password += char
print("DISPLAY THE PASSWORD :- ",password)