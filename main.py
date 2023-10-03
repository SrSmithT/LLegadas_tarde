from flask import Flask, request, render_template
from conexion import *  # Importando conexion BD


app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("llegadastarde.html")


@app.route("/guardar_tarde", methods=["GET", "POST"])
def registrarForm():
    msg = ""
    if request.method == "POST":
        fecha_tarde = request.form["fecha_tarde"]
        id_estudiante = request.form["id_estudiante"]
        hora_llegada_tarde = request.form["hora_llegada_tarde"]

        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)

        cursor.execute(
            "SELECT DATE_FORMAT(fecha_tarde, '%d-%m-%Y') FROM llegadas_tarde_p1"
        )

        sql = "INSERT INTO llegadas_tarde_p1(fecha_tarde, id_estudiante, hora_llegada_tarde) VALUES (%s, %s, %s)"
        valores = (fecha_tarde, id_estudiante, hora_llegada_tarde)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()

        cursor.close()
        conexion_MySQLdb.close()
        msg = "Registro con exito"

        return render_template("llegadastardes.html", msg="Formulario enviado")
    else:
        return render_template("llegadastardes.html", msg="Metodo HTTP incorrecto")


if __name__ == "__main__":
    app.run(debug=True, port=5500)
