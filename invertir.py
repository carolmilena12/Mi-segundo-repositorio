from pila import Pila
def invertir(pila):
    if pila.es_vacia():
        print ("la pila es vacia")
        return None
    else:
        pila_aux1 = Pila()
        pila_aux2 = Pila()
        while not pila.es_vacia():
            pila_aux1.push(pila.pop())
        while not pila_aux1.es_vacia():
            pila_aux2.push(pila_aux1.pop())
        while not pila_aux2.es_vacia():
            pila.push(pila_aux2.pop())

pila1 = Pila()
pila1.push(9)
pila1.push(8)
pila1.push(7)
pila1.push(6)
pila1.mostrar()

invertir(pila1)

pila1.mostrar()
