print("   LA ARENA DEL GLADIADOR")

nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_jugador = 15
danio_enemigo = 12
turno_jugador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    print("\n==============================")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo})")
    print(f"Pociones: {pociones}")
    print("==============================")

    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        if vida_enemigo < 20:
            danio = danio_jugador * 1.5
            print("Golpe crítico")
        else:
            danio = danio_jugador

        vida_enemigo -= danio
        print(f"Atacaste al enemigo por {danio} de daño.")

    elif opcion == 2:
        print("Inicias una ráfaga de golpes")
        for i in range(3):
            vida_enemigo -= 5
            print("Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Usaste una poción (+30 HP)")
        else:
            print("No quedan pociones")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"El enemigo te atacó por {danio_enemigo} de daño.")

print("\n==============================")

if vida_jugador > 0:
    print(f"VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")