import pyodbc
import requests
import json
import time

while(True):    
    file = open("D:\\nrpgiot\\shop.txt", "r")
    text = file.readline().split(",")

    # Asign values to  send

    # Asign database connection details
    server = text[2]

    database = text[3]

    username = text[4]

    password = text[5]
   
    driver=text[6]
    

    
    


    db = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT * From shop ")
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
        row = cursor.fetchone()

   
    time.sleep(10)
