from calc.actual_calc import ActualCalulator
repeat = 'y'
print('''
Enter the operation you are interested in :
1) Enter 1 for performing addition of 2 numbers
2) Enter 2 for performing subraction on 2 numbers
3) Enter 3 for perforiming multiplication on 2 numbers
4) Enter 4 for performing division on 2 numbers
5) Enter 5 to check the parity of a number (Odd/Even)
''')
while repeat == 'y':
    ch = int(input("Enter Your Choice:"))

    c = ActualCalulator()

    if ch == 1:
        c.getsum()
    elif ch == 2:
        c.getdiff()
    elif ch == 3:
        c.getprod()
    elif ch == 4:
        c.getdiv()
    elif ch ==5:
        c.getparity()
    else:
        print("invalid choice")
    repeat = input("Do you want to continue(y/n): ").lower()







