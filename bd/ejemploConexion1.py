import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='studio',
                                         user='root',
                                         password='')
                                        
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)



       # cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)


except Error as e:
    print("Error while connecting to MySQL", e)


