import mysql.connector as mysql

from models import User, Account

# setup connection to database
db = mysql.connect(user='<your_mysql_user_here>', database='<your_mysql_schema_here>', password='<your_mysql_password_here>')

"""
These are your database access functions. They are responsible for direct interactions and queries to the database.
"""


def add_user(user: User):
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
    query_parameters = [user.name, user.email, user.password]
    cursor.execute(query, query_parameters)

    # commit changes
    db.commit()

    # close cursor
    cursor.close()


def get_user_by_email(email: str) -> User:
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "SELECT * FROM user WHERE email = %s"
    cursor.execute(query, [email])

    # get results
    result = cursor.fetchone()

    # close cursor
    cursor.close()

    # return result
    return User(result[0], result[1], result[2], result[3])


def create_user_account(user: User, new_account: Account):
    # insert the new account into our database
    cursor = db.cursor()

    # execute query
    query = "INSERT INTO account (account_number, routing_number, balance, user_id, type) VALUES (%s, %s, %s, %s, %s)"
    query_parameters = [new_account.account_number, new_account.routing_number, new_account.balance, user.id, new_account.type]
    cursor.execute(query, query_parameters)

    # commit changes
    db.commit()

    # close cursor
    cursor.close()


def get_user_account(user: User, account_type: str) -> Account:
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "SELECT * FROM account WHERE user_id = %s AND type = %s"
    query_parameters = [user.id, account_type]
    cursor.execute(query, query_parameters)

    # get results
    result = cursor.fetchone()

    # close cursor
    cursor.close()

    # return result
    return Account(result[0], result[1], result[2], result[3], result[5], result[4])


def update_account_balance(account_id, new_balance):
    # create cursor
    cursor = db.cursor()

    # execute query
    query = "UPDATE account SET balance = %s WHERE id = %s"
    query_parameters = [new_balance, account_id]
    cursor.execute(query, query_parameters)

    # commit changes
    db.commit()

    # close cursor
    cursor.close()
