import datetime


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.llegadas_tarde = []
        self.total_llegadas = 0

    def registrar_llegada_tarde(self):
        fecha_hora_actual = datetime.datetime.now()
        self.llegadas_tarde.append(fecha_hora_actual)
        self.total_llegadas += 1

    def obtener_llegadas_tarde(self):
        return self.llegadas_tarde

    def obtener_total_llegadas(self):
        return self.total_llegadas


estudiantes = {}


def registrar_llegada_tarde():
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")

    if nombre_estudiante in estudiantes:
        estudiantes[nombre_estudiante].registrar_llegada_tarde()
    else:
        estudiantes[nombre_estudiante] = Estudiante(nombre_estudiante)
        estudiantes[nombre_estudiante].registrar_llegada_tarde()

    print(
        f"Llegada tarde registrada para {nombre_estudiante} a las {datetime.datetime.now()}"
    )


def consultar_llegadas_tarde():
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")

    if nombre_estudiante in estudiantes:
        llegadas_tarde = estudiantes[nombre_estudiante].obtener_llegadas_tarde()
        total_llegadas = estudiantes[nombre_estudiante].obtener_total_llegadas()

        print(f"Llegadas tarde de {nombre_estudiante}:")
        for i, llegada in enumerate(llegadas_tarde, start=1):
            print(f"{i}. {llegada}")

        print(f"Total de llegadas tarde: {total_llegadas}")
    else:
        print("El estudiante no existe en la lista.")


while True:
    print("Menú:")
    print("1. Registrar llegada tarde")
    print("2. Consultar llegadas tarde de un estudiante")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        registrar_llegada_tarde()
    elif opcion == "2":
        consultar_llegadas_tarde()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")


print("lista de estudiantes")
estu = ["santiago,samuel,galvis,brandon,pacho,condor,johan"]
print(estu)


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.llegadas_tarde = 0

    def registrar_llegada_tarde(self):
        self.llegadas_tarde += 1

    def obtener_llegadas_tarde(self):
        return self.llegadas_tarde


estudiantes = {}


def registrar_llegada_tarde():
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")

    if nombre_estudiante in estudiantes:
        estudiantes[nombre_estudiante].registrar_llegada_tarde()
    else:
        estudiantes[nombre_estudiante] = Estudiante(nombre_estudiante)
        estudiantes[nombre_estudiante].registrar_llegada_tarde()

    print(f"Llegada tarde registrada para {nombre_estudiante}")


def consultar_llegadas_tarde():
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")

    if nombre_estudiante in estudiantes:
        llegadas_tarde = estudiantes[nombre_estudiante].obtener_llegadas_tarde()
        print(f"{nombre_estudiante} ha llegado tarde {llegadas_tarde} veces.")
    else:
        print("El estudiante no existe en la lista.")


while True:
    print("Menú:")
    print("1. Registrar llegada tarde")
    print("2. Consultar llegadas tarde de un estudiante")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        registrar_llegada_tarde()
        lista = {registrar_llegada_tarde}
    elif opcion == "2":
        consultar_llegadas_tarde()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
