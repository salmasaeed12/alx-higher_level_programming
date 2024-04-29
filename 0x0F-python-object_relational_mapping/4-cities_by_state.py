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
            SELECT cities.id, cities.name, states.name FROM cities
            JOIN states ON states.id = cities.state_id
            ORDER BY cities.id ASC;
        """

    cursor.execute(my_select_query)

    my_rows = cursor.fetchall()

    for row in my_rows:
        print(row)

    cursor.close()
    connection.close()
