from time import sleep
from user import User
from random import randint
def addAcount():
    name = input("Enter Name: ")
    account = input("Enter the 10 digit acount number: ")
    pin = input("Enter the secret pin of your bank acount: ")
    print("Adding User to our new system")
    sleep(2)
    User(name, account, pin)

def addNewUser():
    name = input("Enter Name: ")
    account = randint(11111111,99999999)
    pin = randint(1111,9999)
    sleep(3)
    print(f"{name}Please note  your Acount number is {account} and pin is {pin}")
    User(name, account, pin)
    



    

