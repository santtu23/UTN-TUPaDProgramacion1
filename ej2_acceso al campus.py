usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    print(f"\nIntento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada.")
else:
    opcion = ""

    while opcion != "4":
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        if int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
            continue

        if opcion == "1":
            print("Inscripto")

        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")
            confirmar = input("Confirmar clave: ")

            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
            elif nueva_clave != confirmar:
                print("Error: las claves no coinciden.")
            else:
                clave_correcta = nueva_clave
                print("Clave actualizada correctamente.")

        elif opcion == "3":
            print("¡Seguí adelante, vas bien!")

        elif opcion == "4":
            print("Saliendo del sistema...")