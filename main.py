import clases as cl
import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def esperar_tecla():
    input("\n\nPresione enter para continuar. \n")
    clear()


crucero_gestor = cl.Gestor()
crucero_gestor.iniciar()


def menu_agregar(cubierta):
    if cubierta != "1" and cubierta != "2" and cubierta != "3":
        print("\n Ingresaste un valor incorrecto.")
        esperar_tecla()
    
    else:
        while True:
            clear()
            crucero_gestor.mostrar_habitaciones_disponibles(cubierta)
            try:
                num = int(input("\n Ingrese el número de la habitación que desea: "))
                for i in crucero_gestor.habitaciones:
                    if num == i.numero:
                        clear()
                        print("registre al usuario de la reserva")
                        print("------------------------------------\n")
                        nombre = input("Ingrese nombre: ")
                        id = int(input("ingrese identificacion: "))
                        edad = int(input("Ingrese edad: "))
                        user = cl.User(nombre, id, edad)
                
                        acompañantes = []
                        for x in range(i.tipo - 1):
                            clear()
                            print(f"\nIngrese acompañante {x + 1}")
                            print("-------------------------------\n")
                            nombre_a = input("Ingrese nombre: ")
                            id_a = int(input("ingrese identificacion: "))
                            edad_a = int(input("Ingrese edad: "))
                            user_a = cl.User(nombre_a, id_a, edad_a)
                            acompañantes.append(user_a)

                        clear()
                        crucero_gestor.agregar_reserva(num, user, acompañantes)
                        esperar_tecla()
                        return
                clear()
                print(f"No se encontro habitacion con numero {num}")
                esperar_tecla()
            except (ValueError, TypeError):
                print("\n Ingresaste un valor incorrecto, ingresa de nuevo.")
                esperar_tecla()
                clear()


def menu():
    while True:
        clear()
        seleccion = input("""
        1. Agregar reserva

        2. Eliminar reserva

        3. Mostrar reservas

        4. Mostrar habitaciones disponibles

        5. Buscar reserva

        6. Salir
        ----------------------------------------
        Ingrese una opción: """)

        if seleccion == "1":
            while True:
                clear()
                cubierta = input("""
        Ingrese el tipo de cubierta para la reserva:

        1. BASICA
        - precio base: 300000

        2. Normal
        - precio base: 500000

        3. Premium
        - precio base: 700000
        --------------------------------
        Ingrese una opción: """)

                menu_agregar(cubierta)
                break

        elif seleccion == "2":
            clear()
            id = input("Ingrese el ID de la reserva a eliminar: ")
            clear()
            crucero_gestor.cancelar_reserva(id.upper())
            esperar_tecla()

        elif seleccion == "3":
            clear()
            crucero_gestor.mostrar_reservas()
            esperar_tecla()

        elif seleccion == "4":
            clear()
            crucero_gestor.mostrar_habitaciones_disponibles()
            esperar_tecla()

        elif seleccion == "5":
            clear()
            if crucero_gestor.reservas:
                id = input("Ingrese el ID de la reserva que desea buscar: ")
                clear()
                crucero_gestor.buscar_reserva(id.upper())
            else:
                print("Todavia no se ha ingresado reservas.")
            esperar_tecla()

        elif seleccion == "6":
            break

menu()
