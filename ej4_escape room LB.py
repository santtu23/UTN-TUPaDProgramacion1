print("   ESCAPE ROOM: LA BÓVEDA")

nombre = input("Ingrese nombre del agente: ")

while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("Ingrese nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("Sistema bloqueado por alarma. PERDISTE.")
        break

    print("\n==============================")
    print(f"Agente: {nombre}")
    print(f"Energía: {energia} | Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")
    print("==============================")

    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: opción inválida")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        if forzar_seguidas == 3:
            alarma = True
            print("Forzaste 3 veces seguidas. La cerradura se trabó y se activó la alarma.")
            continue

        if energia < 40:
            numero = input("Riesgo de alarma! Elegí número (1-3): ")

            while not numero.isdigit() or int(numero) not in [1, 2, 3]:
                print("Error: número inválido")
                numero = input("Elegí número (1-3): ")

            if int(numero) == 3:
                alarma = True
                print("Se activó la alarma!")

        if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura!")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print("Hackeando...")

        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Hackeo completo! Se abrió una cerradura.")

    elif opcion == 3:
        tiempo -= 1
        forzar_seguidas = 0

        energia += 15
        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
            print("La alarma te afecta mientras descansás (-10 extra)")

        print("Descansaste y recuperaste energía.")

print("\n==============================")

if cerraduras_abiertas == 3:
    print("VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA! Te quedaste sin recursos.")