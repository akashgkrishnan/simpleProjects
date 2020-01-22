from magic import addAcount, addNewUser

print("1) Register an existing acount: ")
print("2) Create an acount: ")
print("3) Check Balance: ")
print("4) Withdraw money: ")
choice = int(input("Choice: "))

if choice == 1:
    addAcount()
elif choice == 2:
    addNewUser()



