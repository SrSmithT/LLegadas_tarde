import mysql.connector


def connectionBD():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysqlpasswordAAA1_",
        database="Pruebas",
        port="3306",
    )

    if mydb:
        print("Conexión exitosa")
    else:
        print("Error en la conexión a BD")
    return mydb
