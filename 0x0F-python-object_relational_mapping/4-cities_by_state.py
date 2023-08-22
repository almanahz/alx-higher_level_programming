#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Entry point to database.
    """

    connector = MySQLdb.connect(host="localhost", user=argv[1],
                                port=3306, passwd=argv[2], db=argv[3])

    with connector.cursor() as cur:
        cur.execute("""
            SELECT
                c.id, c.name, s.name
            FROM
                cities c
            JOIN
                states s
            ON
                c.states_id = states.id
            ORDER BY
                c.id ASC
        """)

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
