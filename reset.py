import pyodbc
import time
while(True):    
    file = open("D:\\nrpgiot\\shop.txt", "r")
    text = file.readline().split(",")
    print(text)

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

    # Get location details from a site using its api
  

    db = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = db.cursor()
    with cursor.execute("DELETE From shop"):
        print("deleted")
    time.sleep(60)