lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


operador = input("Nombre del operador: ")
while not operador.isalpha():
    operador = input("Error. Solo letras: ")

opcion = ""

while opcion != "5":

    print("\n1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Error. Solo letras: ")

        if dia == "1":
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Ese nombre ya tiene turno el lunes")
            else:
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("No hay turnos disponibles el lunes")

        elif dia == "2":
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Ese nombre ya tiene turno el martes")
            else:
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("No hay turnos disponibles el martes")

        else:
            print("Día inválido")

    elif opcion == "2":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        nombre = input("Nombre a cancelar: ")
        while not nombre.isalpha():
            nombre = input("Error. Solo letras: ")

        if dia == "1":
            if nombre == lunes1:
                lunes1 = ""
            elif nombre == lunes2:
                lunes2 = ""
            elif nombre == lunes3:
                lunes3 = ""
            elif nombre == lunes4:
                lunes4 = ""
            else:
                print("No existe ese turno en lunes")

        elif dia == "2":
            if nombre == martes1:
                martes1 = ""
            elif nombre == martes2:
                martes2 = ""
            elif nombre == martes3:
                martes3 = ""
            else:
                print("No existe ese turno en martes")

        else:
            print("Día inválido")

    elif opcion == "3":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("\nAgenda Lunes:")
            print("Turno 1:", lunes1 if lunes1 != "" else "Libre")
            print("Turno 2:", lunes2 if lunes2 != "" else "Libre")
            print("Turno 3:", lunes3 if lunes3 != "" else "Libre")
            print("Turno 4:", lunes4 if lunes4 != "" else "Libre")

        elif dia == "2":
            print("\nAgenda Martes:")
            print("Turno 1:", martes1 if martes1 != "" else "Libre")
            print("Turno 2:", martes2 if martes2 != "" else "Libre")
            print("Turno 3:", martes3 if martes3 != "" else "Libre")

        else:
            print("Día inválido")

    elif opcion == "4":

        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        print("\nResumen:")
        print("Lunes ocupados:", ocupados_lunes, "Disponibles:", 4 - ocupados_lunes)
        print("Martes ocupados:", ocupados_martes, "Disponibles:", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")

    elif opcion != "5":
        print("Opción inválida")

print("Sistema cerrado")