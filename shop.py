import pyodbc
import requests
import json
import time
file = open("shop.txt", "r")
text = file.readline().split(",")
print(text)
# Asign values to  send
nodeId = text[0]
print(nodeId)
tier = text[1]
print(tier)
# Asign database connection details
server = text[2]
print(server)
database = text[3]
print(database)
username = text[4]
print(username)
password = text[5]
print(password)
driver=text[6]
print(driver)   
while(True):       


    db = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT * From shop where nodeID="+nodeId)
    row = cursor.fetchone()
    print(row)    
    if row!=None:
        print("Allready there")
        
    else:
        # Get location details from a site using its api    
   
        j=  json.loads((requests.get(text[7])).text)
        latitude,longitude = str(j['latitude']),str(j['longitude'])
        #SQL query to INSERT a record into the database
        with cursor.execute("INSERT INTO  shop(nodeID,tier, latitude ,longitude)  VALUES ("+nodeId+","+tier+","+latitude+","+longitude+")"): 
            print ('Successfuly Inserted!')    
    time.sleep(300)
