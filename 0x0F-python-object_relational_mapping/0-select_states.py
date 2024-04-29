#!/usr/bin/python3

"""my module that link MySQLdb with python without ORM"""


import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        passwd=args[2],
        db=args[3],
        charset="utf8")

    cursor = connection.cursor()

    query = """
    SELECT * FROM states
    ORDER BY id ASC;
    """
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
