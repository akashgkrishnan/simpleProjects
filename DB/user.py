import sqlite3

def addAcount(name, acount_no, pin, bank_balance = 0):
    conn = sqlite3.connect("Bank.db")
    conn.cursor()
    data = (name, acount_no, bank_balance, pin)
    query = f'INSERT INTO CUSTOMER_DTL VALUES (?,?,?,?)'
    conn.execute(query, data)
    conn.commit()
    conn.close()
    print(f"{name} has been added to our DB:")

def withdraw_money(amount):
    conn = sqlite3.connect("Bank.db")
    c = conn.cursor()
    acount_no = input('Enter acount number: ')
    pin = input('Enter Pin: ')
    data = acount_no,pin
    query = 'SELECT bank_balance from CUSTOMER_DTL where acount_no = ? and pin = ?'
    c.execute(query,data)
    for i in c.fetchone():
        available_balance = i - amount
    print(f"remaining balance = {available_balance}")
    data = (available_balance, acount_no, pin)
    query = 'UPDATE CUSTOMER_DTL SET BANK_BALANCE = ? WHERE ACOUNT_NO = ? AND PIN = ?'
    c.execute(query,data)
    conn.commit()
    conn.close



def get_bank_balance():
    conn = sqlite3.connect("Bank.db")
    c = conn.cursor()
    acount_no = input('Enter acount number: ')
    pin = input('Enter Pin: ')
    data = (acount_no, pin)
    query = 'SELECT bank_balance from CUSTOMER_DTL where acount_no = ? and pin = ?'
    c.execute(query,data)
    for i in c.fetchone():
        available_balance = i
    print(f" Available Balance in your acount: {available_balance}")
        

    
def deposit_money(amount):
    conn = sqlite3.connect("Bank.db")
    c = conn.cursor()
    acount_no = input('Enter acount number: ')
    pin = input('Enter Pin: ')
    data = (acount_no, pin)
    query = 'SELECT bank_balance from CUSTOMER_DTL where acount_no = ? and pin = ?'
    c.execute(query,data)
    for i in c.fetchone():
        available_balance = i + amount
    print(f"remaining balance = {available_balance}")
    data = (available_balance, acount_no, pin)
    query = 'UPDATE CUSTOMER_DTL SET BANK_BALANCE = ? WHERE ACOUNT_NO = ? AND PIN = ?'
    c.execute(query,data)
    conn.commit()
    conn.close

        

