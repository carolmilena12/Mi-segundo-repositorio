from pila import Pila
from producto import Producto

def obtenerMayorPrecio(pila):
    if pila.es_vacia():
        return None
    pila_aux = Pila()
    item = "polera"
    contador = 0
    
    
    while not pila.es_vacia():
        elemento = pila.pop()
        if item == elemento.get_nombre():
            contador = contador + 1
        pila_aux.push(elemento)

    while not pila_aux.es_vacia():
        pila.push(pila_aux.pop())

    return contador

pila_productos = Pila()
pila_productos.push(Producto(1,"pantalon", 670.0))
pila_productos.push(Producto(2,"zapatos",350.0))
pila_productos.push(Producto(3,"camisa",150.0))
pila_productos.push(Producto(4,"polera",50.5))
pila_productos.push(Producto(1,"pantalon",300.0))



print ("La pila antes: ", pila_productos.mostrar())

contador1 = obtenerMayorPrecio(pila_productos)

print (contador1 )
