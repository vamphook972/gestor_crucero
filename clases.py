class Habitacion:
    def __init__(self, numero, cubierta, tipo, precio):
        self.numero = numero
        self.cubierta = cubierta
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        return f"""
        numero: {self.numero}
        cubierta: {self.cubierta}
        cantidad de personas por cuarto: {self.tipo}
        precio: {self.precio}
        """


class User:
    def __init__(self, nombre, id, edad):
        self.nombre = nombre
        self.id = id
        self.edad = edad

    def __str__(self):
        return f"""
        nombre: {self.nombre}
        documento: {self.id}
        edad: {self.edad}
        """


class Reserva:
    def __init__(self, id, habitacion, user, acompañantes):
        self.id = id
        self.habitacion = habitacion
        self.user = user
        self.acompañantes = acompañantes

    def __str__(self):
        return f"""
    - id de la reserva: {self.id}

    - usuario de la reserva:
        {self.user}
    - habitacion: 
        {self.habitacion}
        """


class Gestor:
    def __init__(self):
        self.ids = [i + x for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for x in "123456789"]
        self.habitaciones = []
        self.reservas = []

    def iniciar(self):
        capacidad_habitaciones = [2, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        for i in range(30):
            if i < 10:
                precio_base = 300000
                habitacion = Habitacion(
                    100 + i + 1,
                    "Economica",
                    capacidad_habitaciones[i],
                    precio_base * capacidad_habitaciones[i],
                )
                self.habitaciones.append(habitacion)

            elif i >= 10 and i < 20:
                precio_base = 500000
                habitacion = Habitacion(
                    200 + i - 10 + 1,
                    "Normal",
                    capacidad_habitaciones[i - 10],
                    precio_base * capacidad_habitaciones[i - 10],
                )
                self.habitaciones.append(habitacion)

            elif i >= 20 and i < 30:
                precio_base = 700000
                habitacion = Habitacion(
                    300 + i - 20 + 1,
                    "Premium",
                    capacidad_habitaciones[i - 20],
                    precio_base * capacidad_habitaciones[i - 20],
                )
                self.habitaciones.append(habitacion)

    def agregar_reserva(self, num_habitacion, users, acompañantes):
        for i in self.habitaciones:
            if i.numero == num_habitacion:
                self.reservas.append(Reserva(self.ids[0], i, users, acompañantes))
                self.habitaciones.remove(i)
                print(f"""
                |-----------------------------------------------|
                |   Reserva con ID: {self.ids[0]} agregada correctamente   |
                |-----------------------------------------------|
                """)
                self.ids.remove(self.ids[0])

    def cancelar_reserva(self, id):
        for i in self.reservas:
            if i.id == id:
                self.habitaciones.sort(key=lambda hab: hab.numero)
                self.ids.append(id)
                self.ids.sort()
                self.reservas.remove(i)
                print(f"""
                |--------------------------------------|
                |   Reserva con ID: {self.ids[0]} fue eliminada   |
                |--------------------------------------|
                """)
                return
        print(f"No se encontró una reserva con el ID {id}.")

    def mostrar_reservas(self):
        if self.reservas:
            for i in self.reservas:
                print("------------------------------------------")
                print(i)
                print("--------------------------------------- \n")
        else:
            print("\n Todavia no se han ingresado reservas. \n")

    def mostrar_habitaciones_disponibles(self, seleccion=None):
        if seleccion == "1":
            print("\n Cubierta Economica: \n")
            contador = 0
            for i in self.habitaciones:
                if i.cubierta == "Economica":
                    contador += 1
                    print(i)
            print(
                f"total de habitaciones de cubierta economica disponibles: {contador}"
            )
            print("------------------------------------------------------------")

        elif seleccion == "2":
            print("\n Cubierta Normal: \n")
            contador = 0
            for i in self.habitaciones:
                if i.cubierta == "Normal":
                    contador += 1
                    print(i)
            print(f"total de habitaciones de cubierta normal disponibles: {contador}")
            print("---------------------------------------------------------")

        elif seleccion == "3":
            print("\n Cubierta Premium: \n")
            contador = 0
            for i in self.habitaciones:
                if i.cubierta == "Premium":
                    contador += 1
                    print(i)
            print(f"total de habitaciones de cubierta premium disponibles: {contador}")
            print("----------------------------------------------------------")

        elif not seleccion:
            print("\n Cubierta Economica: \n")
            contador = 0
            for i in self.habitaciones:
                if i.cubierta == "Economica":
                    contador += 1
                    print(i)
            print(
                f"total de habitaciones de cubierta economica disponibles: {contador}"
            )
            print("------------------------------------------------------------")

            print("\n Cubierta Normal: \n")
            contador = 0
            for i in self.habitaciones:
                if i.cubierta == "Normal":
                    contador += 1
                    print(i)
            print(f"total de habitaciones de cubierta normal disponibles: {contador}")
            print("---------------------------------------------------------")

            print("\n Cubierta Premium: \n")
            contador = 0
            for i in self.habitaciones:
                if i.cubierta == "Premium":
                    contador += 1
                    print(i)
            print(f"total de habitaciones de cubierta premium disponibles: {contador}")
            print("----------------------------------------------------------")

            print(f"\n total de habitaciones disponibles: {len(self.habitaciones)} \n")

        else:
            print("Seleccion no permitida.")

    def buscar_reserva(self, id):
        for i in self.reservas:
            if i.id == id:
                print(i)
                return
        else:
            print(f"No se encontro reserva con id: {id}")
