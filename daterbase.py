import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS new_user(fName TEXT, sName TEXT,phonenumber INTEGER')
