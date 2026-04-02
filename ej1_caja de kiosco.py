print("====================================")
print("        CAJA DEL KIOSCO 🧾")
print("====================================")

nombre_cliente = input("Bienvenido a Zoco, ingrese su nombre: ").title()

while not nombre_cliente.replace(" ", "").isalpha() or nombre_cliente.strip() == "":
    print("------------------------------------")
    print("Error: solo letras y no vacío.")
    nombre_cliente = input("Intente nuevamente: ").title()

print("====================================")
print("Cliente:", nombre_cliente)
print("====================================")

cantidad_productos = input("Ingrese la cantidad de productos: ")

while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("------------------------------------")
    print("Error: número mayor a 0.")
    cantidad_productos = input("Ingrese nuevamente: ")

cantidad_productos = int(cantidad_productos)

print("====================================")
print("        CARGA DE PRODUCTOS")
print("====================================")

total_sin_descuento = 0
total_con_descuento = 0

for p in range(cantidad_productos):
    print("------------------------------------")
    print(f"Producto {p+1}")

    precio = input("Precio: ")

    while not precio.isdigit() or int(precio) <= 0:
        print("Error: precio inválido.")
        precio = input("Precio: ")

    precio = int(precio)

    total_sin_descuento += precio

    descuento = input("¿Descuento? (S/N): ").lower()

    while descuento not in ["s", "n"]:
        print("Error: solo S o N.")
        descuento = input("¿Descuento? (S/N): ").lower()

    if descuento == "s":
        precio_con_descuento = precio * 0.9
        print("Se aplicó 10% de descuento")
    else:
        precio_con_descuento = precio
        print("Sin descuento")

    total_con_descuento += precio_con_descuento

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos

print("====================================")
print("           RESULTADO FINAL")
print("====================================")
print(f"Total sin descuentos:   ${total_sin_descuento}")
print(f"Total con descuentos:   ${total_con_descuento:.2f}")
print(f"Ahorro total:           ${ahorro:.2f}")
print(f"Promedio por producto:  ${promedio:.2f}")
print("====================================")
print("       ¡Gracias por comprar!")
print("====================================")