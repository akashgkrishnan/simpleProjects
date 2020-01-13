from random import randint
from time import sleep
print('HI I GENERATE AWESOME PASSWORD')

length = int(input("How long do you want your password to be:"))
password = []
while len(password) <= length:
    num = randint(0, 91)
    if num < 10:
        password.append(str(num))
    if num >= 65 and num <=90:
        if num % 2 == 0:
            password.append(str(chr(num).lower()))
        else:
            password.append(str(chr(num).upper()))

for i in range(5,0,-1):
    print("\n"*35)
    print(f"Generating an awesome pass in {i} seconds")
    print("\n"*30)
    sleep(1)
print(f"Your aswesome secret password is {''.join(password)}")
print("\n"*30)