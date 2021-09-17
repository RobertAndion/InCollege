import sqlite3
db = sqlite3.connect('InCollege')

# creates cursor instance. It'll be used to execute queries/commands in the database
c = db.cursor()

### if you want to create the user table
## One time use only, unless you delete the database or the table
c.execute(''' CREATE TABLE users (
        username text PRIMARY KEY,
        password text NOT NULL
    )
''')


### To select and print all records
## SHOULD REMOVE BEFORE SUBMITTING
c.execute('SELECT * FROM users')
# view all selected records
data = c.fetchall()
for row in data:
    print(row)

### if you want to clear the table, for some reason
# sql = 'DELETE FROM users'
# c.execute(sql)
db.commit()