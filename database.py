import sqlite3


conn= sqlite3.connect('test.db') # this will create a db and connect to it. If db already exists, it will connect to it
#conn = sqlite3.connect(':memory:') will create an in-memory database

#create a cursor
c= conn.cursor()

#create a table
#NULL INTEGER TEXT REAL BLOB
c.execute(""" CREATE TABLE companies (
    company_name text,
    province text,   
    registered_office text,
    number_of_employees integer,
    website text,
    email text,
) 
""")