from user import addAcount, withdraw_money, deposit_money, get_bank_balance

print("1) Register an existing acount: ")
print("2) Check Balance: ")
print("3) Withdraw money: ")
print("4) Deposit money")
choice = int(input("Choice: "))

if choice == 1:
    name = input("Enter name: ")
    acount_no = input("Enter acount_no: ")
    pin = input("Enter Age: ")
    addAcount(name, acount_no, pin)

elif choice == 2:
    get_bank_balance()

elif  choice == 3:
    amount = int(input("Enter the amount you want to withdraw: "))
    withdraw_money(amount)
    
elif choice == 4:
    amount = int(input("How muc would you like to deposit to your acount: "))
    deposit_money(amount)

else: 
    print("System not trained for this kind of B.S")




