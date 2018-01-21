#!/usr/bin/python
import MySQLdb
import random
import time

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="slugspace")
cur = db.cursor()

lots = [1, 2, 3]

while True:
    for lot in lots:
        rowLot = cur.execute("SELECT * FROM parking_lots WHERE id = " + str(lot))
        dataLot = cur.fetchone()

        rand = random.randint(0, 1)
        if rand == 0:
            rand = -1

        if rand == -1 and dataLot[3] == 0:
            rand = 1

        filled = dataLot[3] + rand
        cur.execute("INSERT INTO parking_events VALUES (NULL, " + str(lot) + ",  " + str(rand) + ", " + str(filled) + ", NOW())")

        cur.execute("UPDATE parking_lots SET filled = " + str(filled) + ", updated_at = NOW() WHERE id = " + str(lot))
        db.commit()

        print("Car " + ("left" if rand == 0 else "entered") + " " +  dataLot[1] + " parking lot")

    time.sleep(0.5)


