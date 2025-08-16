class Ordenamiento:
    def quick_sort(self,lista, clave):
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

        return Ordenamiento.quick_sort(self,menores, clave) + [pivote] + Ordenamiento.quick_sort(self,mayores, clave)

class Buscar:
    def buscar_valor(self,lista, criterio, valor):
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

opcion = 0
while opcion != 6:
    print("=== Gestion Inventario ===")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Vender producto")
    print("7. Salir")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Opcion no valida")
        continue

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            print("Saliendo del programa")