#!/usr/bin/python3
"""A module that link MySQLdb with python3"""


import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="{}".format(args[1]),
        password="{}".format(args[2]),
        database="{}".format(args[3]),
        charset="utf8"
    )
    cursor = connection.cursor()
    my_select_query = """
            SELECT id, name FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC;
        """.format(args[4])

    cursor.execute(my_select_query)

    my_rows = cursor.fetchall()

    for row in my_rows:
        print(row)

    cursor.close()
    connection.close()
