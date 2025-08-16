from multiprocessing.spawn import prepare


class Producto:
        def __init__(self,codigo:str,nombre:str, categoria:str,precio:float, stock:int ):
           if not codigo.strip():
               raise ValueError("El codigo no puede quedar en vacio debe llenar este parametro ")
           if not nombre.strip():
               raise ValueError("El nombre no debe quedar en vacio debe llenar este parametro")
           if not categoria.strip():
               raise ValueError("La categoria no debe quedar en vacio debe llenar este parametro")
           if precio<0:
               raise ValueError("El valor no debe ser un valor negativo")
           if stock<0:
               raise ValueError("El stock no debe quedar en negativo")

           self.codigo=codigo
           self.nombre=nombre
           self.categoria=categoria
           self.precio=precio
           self.stock=stock
        def actualizar_Precio(self, nuevo_precio:float):
            if nuevo_precio<0:
                raise ValueError("El precio no puede ser negativo")
            self.precio=nuevo_precio
        def actualizar_Stock(self,nuevo_stock:int):
            if nuevo_stock<0:
                raise ValueError("El nuevo stock no puede ser negativo")
            self.stock=nuevo_stock

        def __str__(self):
            return f"[{self.codigo}] {self.nombre} | Cat: {self.categoria} | Precio: Q{self.precio:.2f} | Stock: {self.stock}"

    class Inventario:
        def __init__(self):
            self.productos={}

        def Agregar_Producto(self):
            try:
                cantidad = int(input("Ingrese la cantidad de productos ingresados: "))
                if cantidad < 0:
                    print("El valor no puede ser negativo")
                    return
            except ValueError:
                print("Debe ingresar un dato valido")
                return

            for i in range(cantidad):
                print(f"Producto #{i + 1}")
                codigo = input("Ingrese el codigo del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                categoria = input("Ingrese el tipo de categoria de producto(Limpieza,Comida o Juguetes): ")
                try:
                    precio = float(input("Precio: "))
                    stock = int(input("Stock: "))
                except ValueError:
                    print(" Precio o stock inválido, producto no agregado.")
                    continue
                try:
                    if codigo in self.productos:
                        raise ValueError("El codigo que usted ingreso ya se encuentra registrado")
                    producto = Producto(codigo, nombre, categoria, precio, stock)
                    self.productos[codigo] = producto
                    print("Los datos fueron registrados correctamente")
                except ValueError as e:
                    print(f"Error: {e}")

        def lista_Productos(self):
            if not self.productos:
                print("Aun no se ha registrado ningun producto")
                return
            for prod in self.productos.values():
                print(prod)

    class Ventas:
        def __init__(self, inventario:Inventario):
            self.inventario=inventario
            self.historial=[]

        def vender_Producto(self):
            codigo=input("Ingrese el codigo del producto que se vendera: ")
            if codigo not in self.inventario.productos:
                print("El producto no existe ")

