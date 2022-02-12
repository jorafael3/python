import mysql.connector
from mysql.connector import Error

host = "localhost"
database = "studio"
user =  "root"
passw = ""

connection = mysql.connector.connect(host= host,database=database,user=user,password=passw)

def Test():
    try:

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
        else:
            print("Error")
    except mysql.connector.Error as error:
        print("error de conexion")


Test()

                                        