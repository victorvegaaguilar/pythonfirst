"""Mini tienda: práctica de variables, operadores, strings, listas, tuplas, sets y diccionarios."""

TIENDA = ("Mi Tienda Victor", "Lima", "Perú")  # tuple: datos fijos
productos = []  # list: inventario
categorias = set()  # set: categorías únicas
total_ventas = 0.0  # variable numérica


def leer_entero(mensaje, minimo=0):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
        except ValueError:
            pass
        print(f"Introduce un número entero mayor o igual a {minimo}.")


def leer_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
            if valor >= 0:
                return valor
        except ValueError:
            pass
        print("Introduce un precio válido, mayor o igual a cero.")


def buscar_producto(nombre):
    for producto in productos:
        if producto["nombre"].casefold() == nombre.strip().casefold():
            return producto
    return None


def mostrar_menu():
    print(f"\n===== {TIENDA[0].upper()} =====")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Realizar venta")
    print("5. Ver categorías")
    print("6. Mostrar resumen")
    print("0. Salir")


def main():
    global total_ventas
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip().title()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            if buscar_producto(nombre):
                print("Ese producto ya está registrado.")
                continue
            precio = leer_precio("Precio (S/): ")
            stock = leer_entero("Stock: ")
            categoria = input("Categoría: ").strip().title()
            if not categoria:
                print("La categoría no puede estar vacía.")
                continue
            producto = {"nombre": nombre, "precio": precio, "stock": stock, "categoria": categoria}
            productos.append(producto)
            categorias.add(categoria)
            print("Producto registrado correctamente.")

        elif opcion == "2":
            if not productos:
                print("No hay productos registrados.")
            for producto in productos:
                print(f"{producto['nombre']} | S/ {producto['precio']:.2f} | Stock: {producto['stock']} | {producto['categoria']}")

        elif opcion == "3":
            nombre = input("Producto a buscar: ")
            producto = buscar_producto(nombre)
            if producto:
                print(f"Nombre: {producto['nombre']} | Precio: S/ {producto['precio']:.2f} | Stock: {producto['stock']} | Categoría: {producto['categoria']}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Producto a vender: ")
            producto = buscar_producto(nombre)
            if producto is None:
                print("Producto no encontrado.")
                continue
            cantidad = leer_entero("Cantidad: ", minimo=1)
            if cantidad > producto["stock"]:
                print("Stock insuficiente.")
                continue
            subtotal = producto["precio"] * cantidad
            producto["stock"] -= cantidad
            total_ventas += subtotal
            print(f"Venta realizada. Subtotal: S/ {subtotal:.2f}")

        elif opcion == "5":
            print("Categorías:", ", ".join(sorted(categorias)) if categorias else "ninguna")

        elif opcion == "6":
            print(f"Tienda: {TIENDA[0]}")
            print(f"Ubicación: {TIENDA[1]}, {TIENDA[2]}")
            print(f"Productos registrados: {len(productos)}")
            print(f"Total vendido: S/ {total_ventas:.2f}")

        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
