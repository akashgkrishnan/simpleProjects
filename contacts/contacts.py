import sqlite3
from time import sleep
def menu():
    print("Console Contact Storage App")
    print("1) Add contact: ")
    print("2) View All Contacts: ")
    print("3) Search Contacts: ")
    print("4) Delete contacts: ")
    print("Quit anytime using CTRL+Z")
    print()
    ch = int(input("What would you like to do: "))
    return ch

def save_contact(name, mobile):
    data = (name, mobile)
    c = sqlite3.connect('contacts.db')
    query = f'INSERT INTO CONTACTS VALUES (?,?)'
    c.execute(query,data)
    c.commit()
    c.close()
    sleep(1)
    return "saved to DB"

def search_contact(name):
    data = (name,)
    c = sqlite3.connect('contacts.db')
    query = f'SELECT * FROM CONTACTS WHERE NAME LIKE ?'
    data = c.execute(query, data)
    all_contacts = data.fetchall()
    c.close()
    return all_contacts
   


def delete_contact(name):
    data = (name,)
    print("wE ARE NEW TO THIS SO WE MIGHT DELETE ALL CONTACTS WITH THE SAME NAME...")
    c = sqlite3.connect('contacts.db')
    query = f'DELETE FROM CONTACTS WHERE NAME LIKE ?'
    c.execute(query,data)
    c.commit()
    c.close()
    sleep(1)  
    return "DELETED FROM  DB"

def all_contacts():
    c = sqlite3.connect('contacts.db')
    data = c.execute('SELECT * FROM CONTACTS')
    all_contacts = data.fetchall()
    c.close()
    return all_contacts
    


    
    