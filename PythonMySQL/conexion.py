# import mysql.connector

# mydb = mysql.connector.connect(
#    host="localhost",
#   user="root",
#    password="mysqlpasswordAAA1_",
#    database="Pruebas",
#    port="3306",
# )

# if mydb:
#    print("Conexión exitosa")
# else:
#    print("Error en la conexión a BD")


# cursor = mydb.cursor()

# cursor.execute(
#    "CREATE TABLE llegadas_tarde_p3(fecha_tarde DATE PRIMARY KEY, id_estudiante INT, hora_llegada_tarde TIME)"
# )

# mydb.commit()
# mydb.close()
