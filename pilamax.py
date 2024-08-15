# main.py
from pila import Pila

def obtener_valor_mayor(pila):
    if pila.es_vacia():
        print ("Pila vacia")
        return None
    else: 
        pila_aux = Pila()
        maximo = pila.peek()
        while not pila.es_vacia():
            item=pila.pop()
            if item > maximo:
                maximo=item
            pila_aux.push(item)
        
        while not pila_aux.es_vacia:
            pila.push(pila_aux.pop())
        return maximo
    
pila1 = Pila()
pila1.push('c')
pila1.push('a')
pila1.push('r')
pila1.push('o')
pila1.push('l')

pila1.mostrar()

max= obtener_valor_mayor(pila1)
print (f'El elemento de mayor valor es {max}')


