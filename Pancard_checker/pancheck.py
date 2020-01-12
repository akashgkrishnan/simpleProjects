from sys import exit
from time import sleep
from random import randint





def userdetails():
    first_name = input("Enter Your First name: ").upper()
    last_name = input("Enter your Last Name: ").upper()
    age = int(input("Enter Your age: "))
    if age < 18:
        print("You are too small.. Apply After you are 18")
        sleep(3)
        exit(0)

    while True:
        print("\n"*25)
        purpose = input('''Who is this PAN Card for :
        C for Company, 
        P for Person, 
        H for HUF (Hindu Undivided Family), 
        F for Firm, 
        A for Association of Persons (AOP), 
        T for AOP (Trust), 
        B for Body of Individuals (BOI), 
        L for Local Authority, 
        J for Artificial Juridical Person 
        G for Government.
        Enter: ''')
        if purpose  in ('C', 'P', 'H', 'F', 'A', 'T', 'B', 'J', 'L', 'G'):
            break
        else:
            print("Enter a valid input")
            sleep(2)
    for i in range(5,0,-1):
        print("\n"*50)
        print(f"Please wait while i generate an Awesome Pan number for you in {i} seconds..")
        sleep(1)
    print("\n"*20)
    print(f"{first_name} {last_name} Your Pan card has been generated: \n Your pan number is   {panvalidation(last_name[0], purpose)}")
    print("\n"*10)


def panvalidation(l_name, p):
    pan = []
    for i in range(10):
        if i < 3:
            pan.append(chr(randint(65, 90)))
        elif i == 3:
            pan.extend([p, l_name])
    pan.append(str(randint(1111, 9999)))
    pan.append(chr(randint(65, 90)))
    return ''.join(pan)


userdetails()