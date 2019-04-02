# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 01:00:17 2019

@author: Florian
"""

#!/usr/bin/python3.6
import mysql.connector
import api_query as aq

db = "weather_db"
tbl = "weather_table"
mydb = mysql.connector.connect(host="localhost")
mycursor = mydb.cursor()

def add_to_db(item):
    wtr = aq.owm(item)
    print(wtr)
    # create database if not present
    mycursor.execute("CREATE DATABASE IF NOT EXISTS " + db)
    mycursor.execute("use " + db)
    # create table if not present
    mycursor.execute("CREATE TABLE IF NOT EXISTS " + tbl + " (query_index INT PRIMARY KEY AUTO_INCREMENT, city CHAR(30), country CHAR(5), temp_C INT(3), weather CHAR(20), last_update CHAR(30))")

    # insert rows
    sql = "INSERT INTO " + tbl + " (city,country,temp_C,weather,last_update) VALUES (%s, %s, %s, %s, %s)"
    val = (wtr[0], wtr[1], wtr[2], wtr[3], wtr[4])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted into", tbl, "of", db,".")
    print("The last inserted id was: ", mycursor.lastrowid)

def query_db(query):
    mycursor.execute("use " + db)
    mycursor.execute("SELECT * FROM " + tbl + " WHERE city=" + '"' + query + '"')
    result = mycursor.fetchall()
    for row in result:
        print(row)

