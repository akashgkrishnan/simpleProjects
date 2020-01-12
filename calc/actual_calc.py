class ActualCalulator:
    def getsum(self):
        print("\n"*40)
        print("SUM")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("\n"*10)
        print(f"The sum of {a} and {b} is = {a+b}")
        print("\n"*10)


    def getdiff(self):
        print("\n"*40)
        print("DIFFERENCE")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("\n"*10)
        print(f"The differnce of {a} and {b} is = {a-b}")
        print("\n"*10)


    def getprod(self):
        print("\n"*40)
        print("PRODUCT")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("\n"*10)
        print(f"The product of {a} and {b} is = {a*b}")
        print("\n"*10)


    def getdiv(self):
        print("\n"*40)
        print("DIVISION")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("\n"*10)
        print(f"The division of {a} and {b} is = {a/b}")
        print("\n"*10)


    def getparity(self):
        print("\n"*40)
        print("PARITY")
        a = int(input("Enter the  number: "))
        print("\n"*10)
        if a % 2 ==0:
            print(f"The number {a} is Even")
            print("\n" * 10)

        else:
            print(f"The number {a} is Odd")
            print("\n" * 10)


