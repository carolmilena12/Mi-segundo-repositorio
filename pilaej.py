class Pila():
    def __init__(self):
        self.datos=[]
#Llena la pila de elementos
    def push(self, dato):
        self.datos.append(dato)
        #print (f'El elemento {dato} ha sido apilado')
#Saca los elementos tipo LIFO
    def pop(self):
        if not self.es_vacia():
            dato = self.datos.pop()
           # print (f'El elemento {dato} ha sido desapilado')
            return dato
        else:
            print('La pila ya se encuentra vacia')
            return None

# Verifica si la pila esta vacia
    def es_vacia(self):
        return len(self.datos)==0
    
# Mostrar la pila
    def mostrar(self):
        if not self.es_vacia():
            for dato in reversed(self.datos):
                print (dato)
        else: 
            print ("La pila esta vacia")

pila1 = Pila()
pila1.push(20)
pila1.push(10)
pila1.push(40)
pila1.push(50)

pila1.pop()
pila1.pop()


pila1.mostrar()



        