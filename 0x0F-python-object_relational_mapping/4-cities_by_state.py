#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities AS c
            JOIN
                states AS s
            ON
                c.state_id = s.id
            ORDER BY
                cities.id ASC
        """)

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
