import sqlite3
from datetime import datetime
from web_server import conn


def init_db():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                (payer text, points integer, timestamp text)''')
    conn.commit()

def show_db():
    c = conn.cursor()
    c.execute('''SELECT * FROM transactions ORDER BY timestamp DESC''')
    print("Fetch..")
    print(c.fetchall())

def insert_transaction(payer, points, timestamp):
    c = conn.cursor()
    record = (payer, points, timestamp)
    print("Inserting..", record)
    c.execute('''INSERT INTO transactions VALUES (?,?,?)''', record)


def spend_points(owed_points):
    c = conn.cursor()

    usage = {}
    c.execute('''SELECT payer, points FROM transactions ORDER BY timestamp ASC''')
    result = c.fetchone()
 
    while (result != None) and (owed_points > 0):
        payer, owned_points = result
        
        if payer not in usage:
            usage[payer] = 0

        
        if owed_points > owned_points:
            
            owed_points -= owned_points
            usage[payer] -= owned_points
        else:
            
            usage[payer] -= owed_points
            owed_points = 0

        
        result = c.fetchone()

    return usage

def view_balance():
    c = conn.cursor() 
    balance = {}
     
    c.execute('''SELECT payer, points FROM transactions ORDER BY timestamp ASC''')
    result = c.fetchone()
 
    
    while result != None:
        payer, owned_points = result
        
        if payer not in balance:
            balance[payer] = 0

        balance[payer] += owned_points
        result = c.fetchone()

    return balance

init_db()