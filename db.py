import sqlite3


def create_conenction(db_name):
    db = sqlite3.connect(db_name)
    return db


def create_table(db, sql):
    # creates cursor instance. It'll be used to execute queries/commands in the database
    c = db.cursor()

    # if you want to create the user table
    c.execute(sql)


def create_all_tables(db):
    sql_create_users_table = ''' CREATE TABLE IF NOT EXISTS users (
        username text PRIMARY KEY,
        password text NOT NULL
    )
'''
    create_table(db, sql_create_users_table)
    db.commit()


# To select and print all records
# SHOULD REMOVE BEFORE SUBMITTING
def print_users(db):
    c = db.cursor()
    c.execute('SELECT * FROM users')
    # view all selected records
    data = c.fetchall()
    for row in data:
        print(row)


# if you want to clear the table, for some reason
def delete_users_table(db):
    c = db.cursor()
    sql = 'DELETE FROM users'
    c.execute(sql)
    db.commit()
