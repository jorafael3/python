import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                         database='studio',
                                         user='root',
                                         password='')
                                        
if connection.is_connected():
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM clientes")

        myresult = mycursor.fetchall()       #fetchall () Obtener todos los registros

        for x in myresult:
            print(x)


