#!/usr/bin/python3
"""A module that link MySQLdb with python3"""
import MySQLdb
import sys
args = sys.argv
if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        password=args[2],
        database=args[3],
        charset="utf8"
    )
    cursor = connection.cursor()
    my_select_query = """
            SELECT id, name FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY id ASC;
        """

    cursor.execute(my_select_query)

    my_rows = cursor.fetchall()

    for row in my_rows:
        print(row)

    cursor.close()
    connection.close()
