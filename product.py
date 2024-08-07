class Producto:
    def __init__(self, codigo="", nombre="", precio=0.0, marca=""):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def leer(self):
        self.codigo = input("Ingrese el código del producto: ")
        self.nombre = input("Ingrese el nombre del producto: ")
        self.precio = float(input("Ingrese el precio del producto: "))
        self.marca = input("Ingrese la marca del producto: ")

    def mostrar(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Marca: {self.marca}")

    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_marca(self):
        return self.marca

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_precio(self, precio):
        self.precio = precio

    def set_marca(self, marca):
        self.marca = marca

# Ejemplo de uso
producto = Producto()
producto.leer()
producto.mostrar()
print("Nombre del producto:", producto.get_nombre())
producto.set_precio(99.99)
print("Precio actualizado:", producto.get_precio())
