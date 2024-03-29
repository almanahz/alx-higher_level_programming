#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Entry to the database and list all the states in it
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("SELECT * FROM states")
    rows = curs.fetchall()

    for row in rows:
        print(row)
