class CodigoDuplicadoError(Exception):
    pass


class ProductoNoExisteError(Exception):
    pass


class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int):
        if not codigo.strip():
            raise ValueError("El código no puede quedar vacío.")
        if not nombre.strip():
            raise ValueError("El nombre no puede quedar vacío.")
        if not categoria.strip():
            raise ValueError("La categoría no puede quedar vacía.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def actualizar_Precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = nuevo_precio

    def actualizar_Stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise ValueError("El nuevo stock no puede ser negativo.")
        self.stock = nuevo_stock

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} | Cat: {self.categoria} | Precio: Q{self.precio:.2f} | Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto: Producto):
        if producto.codigo in self.productos:
            raise CodigoDuplicadoError("El código ya existe.")
        self.productos[producto.codigo] = producto

    def eliminar_producto(self, codigo: str):
        if codigo not in self.productos:
            raise ProductoNoExisteError("No se encontró el producto.")
        del self.productos[codigo]

    def actualizar_producto(self, codigo: str, nuevo_precio: float = None, nuevo_stock: int = None):
        if codigo not in self.productos:
            raise ProductoNoExisteError("No se encontró el producto.")
        producto = self.productos[codigo]
        if nuevo_precio is not None:
            producto.actualizar_Precio(nuevo_precio)
        if nuevo_stock is not None:
            producto.actualizar_Stock(nuevo_stock)

    def obtener_lista(self):
        return list(self.productos.values())


class Ventas:
    def __init__(self, inventario: Inventario):
        self.inventario = inventario
        self.historial = []

    def vender(self, codigo: str, cantidad: int):
        if codigo not in self.inventario.productos:
            raise ProductoNoExisteError("No se encontró el producto.")
        producto = self.inventario.productos[codigo]
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if producto.stock < cantidad:
            raise ValueError(f"Stock insuficiente. Disponible: {producto.stock}")
        producto.stock -= cantidad
        total = cantidad * producto.precio
        self.historial.append((producto.codigo, producto.nombre, cantidad, total))
        return total

    def mostrar_historial(self):
        if not self.historial:
            print("No hay ventas registradas.")
            return

        print("\nHISTORIAL DE VENTAS:")
        total_general = 0
        for venta in self.historial:
            codigo, nombre, cantidad, total = venta
            print(f"[{codigo}] {nombre} - {cantidad} unidades - Total: Q{total:.2f}")
            total_general += total
        print(f"\n Total acumulado de ventas: Q{total_general:.2f}")

    def filtrar_por_codigo(self, codigo: str):
        ventas_filtradas = [v for v in self.historial if v[0] == codigo]
        if not ventas_filtradas:
            print("No hay ventas para ese producto.")
            return
        for venta in ventas_filtradas:
            _, nombre, cantidad, total = venta
            print(f"{nombre} - {cantidad} unidades - Q{total:.2f}")


class Ordenamiento:
    def quick_sort(self, lista, clave):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]

        if clave == "nombre":
            menores = [x for x in lista[1:] if x.nombre < pivote.nombre]
            mayores = [x for x in lista[1:] if x.nombre > pivote.nombre]

        elif clave == "precio":
            menores = [x for x in lista[1:] if x.precio < pivote.precio]
            mayores = [x for x in lista[1:] if x.precio > pivote.precio]

        elif clave == "stock":
            menores = [x for x in lista[1:] if x.stock < pivote.stock]
            mayores = [x for x in lista[1:] if x.stock > pivote.stock]

        else:
            print("Criterio de orden inválido")
            return lista

        return self.quick_sort(menores, clave) + [pivote] + self.quick_sort(mayores, clave)


class Buscar:
    def buscar_valor(self, lista, criterio, valor):
        resultados = []
        valor = valor.lower()
        for producto in lista:
            if criterio == "codigo" and producto.codigo.lower() == valor:
                resultados.append(producto)
            elif criterio == "nombre" and valor in producto.nombre.lower():
                resultados.append(producto)
            elif criterio == "categoria" and valor in producto.categoria.lower():
                resultados.append(producto)
        return resultados


class Menu:

    def mostrar_menu(self):
        print("\nMENÚ PRINCIPAL")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar inventario")
        print("5. Registrar venta")
        print("6. Mostrar historial de ventas")
        print("7. Filtrar ventas por código")
        print("8. Salir")


inventario = Inventario()
ventas = Ventas(inventario)
opcion = 0
while opcion != 8:
    mostrar_menu()
    opcion = input("Seleccione una opción: ").strip()

    try:
        match int(opcion):
            case 1:
                print("\n Agregar productos al inventario")
                contador = 0
                productos_agregados = []

                while True:
                    codigo = input(f"\nProducto #{contador + 1} - Código (o 'fin' para terminar): ").strip()
                    if codigo.lower() == "fin":
                        print(f"\n Se agregaron {contador} productos.")
                        if productos_agregados:
                            print("\n Resumen de productos agregados:")
                            for p in productos_agregados:
                                print(p)
                        break

                    if codigo in inventario.productos:
                        print("El código ya existe. Intente con otro.")
                        continue

                    try:
                        nombre = input("Nombre: ").strip()
                        categoria = input("Categoría: ").strip()
                        precio = float(input("Precio: "))
                        stock = int(input("Stock: "))
                        producto = Producto(codigo, nombre, categoria, precio, stock)
                        inventario.agregar_producto(producto)
                        productos_agregados.append(producto)
                        contador += 1
                        print(f"Producto #{contador} agregado.")
                    except ValueError as e:
                        print(f"️ Entrada inválida: {e}")

            case 2:
                codigo = input("Código del producto a eliminar: ")
                inventario.eliminar_producto(codigo)
                print("🗑 Producto eliminado.")

            case 3:
                codigo = input("Código del producto a actualizar: ")
                nuevo_precio = input("Nuevo precio (dejar vacío si no cambia): ")
                nuevo_stock = input("Nuevo stock (dejar vacío si no cambia): ")
                precio = float(nuevo_precio) if nuevo_precio else None
                stock = int(nuevo_stock) if nuevo_stock else None
                inventario.actualizar_producto(codigo, precio, stock)
                print(" Producto actualizado.")

            case 4:
                productos = inventario.obtener_lista()
                if not productos:
                    print(" Inventario vacío.")
                else:
                    print("\n INVENTARIO:")
                    for p in productos:
                        print(p)

            case 5:
                codigo = input("Código del producto: ")
                cantidad = int(input("Cantidad a vender: "))
                total = ventas.vender(codigo, cantidad)
                print(f"Venta registrada. Total: Q{total:.2f}")

            case 6:
                ventas.mostrar_historial()

            case 7:
                codigo = input("Código del producto: ")
                ventas.filtrar_por_codigo(codigo)

            case 8:
                print("¡Hasta luego!")
                break
            case _:
                print(" Opción inválida.")

    except CodigoDuplicadoError as e:
        print(f"Error: {e}")
    except ProductoNoExisteError as e:
        print(f" Error: {e}")
    except ValueError as e:
        print(f"Error de entrada: {e}")
    except Exception as e:
        print(f" Error inesperado: {e}")
