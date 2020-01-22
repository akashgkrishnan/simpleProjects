import sqlite3

class User:
    def __init__(self, name, acount_no, pin, bank_balance = 0):
        self.name = name
        self.acount_no = acount_no
        self.bank_balance = bank_balance
        self.pin = pin
        conn = sqlite3.connect("Bank.db")
        conn.cursor()
        data = (self.name, self.acount_no, self.bank_balance, self.pin)
        query = f'INSERT INTO CUSTOMER_DTL VALUES (?,?,?,?)'
        conn.execute(query, data)
        conn.commit()
        conn.close()
        print(f"{self.name} has been added to our DB:")

    def withdraw_money(self, amount):
        self.bank_balance -= amount
    
    def get_bank_balance(self):
        return self.bank_balance

    def get_acount_no(self):
        return self.acount_no
    
    def deposit_money(self):
        pass

