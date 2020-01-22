import sqlite3
conn = sqlite3.connect("Bank.db")
c = conn.cursor()
c.execute('''CREATE TABLE CUSTOMER_DTL
(name text, acount_no integer, bank_balance integer, pin integer)
''')
conn.commit()
conn.close()

