class CodigoDuplicadoError(Exception):
    pass

class ProductoNoExisteError(Exception):
    pass

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
            producto.actualizar_precio(nuevo_precio)
        if nuevo_stock is not None:
            producto.actualizar_stock(nuevo_stock)

    def obtener_lista(self):
        return list(self.productos.values())
