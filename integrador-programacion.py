# con esta funcion estaremos creando un nodo como lista [valor, izquierda, derecha]
def crear_nodo(valor): 
    return [valor, None, None]

# con esta funcion insertamos un valor en el arbol
def insertar(arbol, valor):
    if arbol is None:
        return crear_nodo(valor)
    if valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor)
    else:
        arbol[2] = insertar(arbol[2], valor)
    return arbol

# recorrido inorden: izquierda -> raiz -> derecha
def inorden(arbol):
    if arbol is not None:
        inorden(arbol[1])
        print(arbol[0], end=' ')
        inorden(arbol[2])

# recorrido postorden: izquierda -> derecha -> raiz
def preorden(arbol):
    if arbol is not None:
        print(arbol[0], end=' ')
        preorden(arbol[1])
        preorden(arbol[2])

# recorrido postorden: izquierda -> derecha -> raiz
def postorden(arbol):
    if arbol is not None:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0], end=' ')


# ejemplo practico
valores = [20, 80, 60, 50, 30, 10, 90, 70, 40]
arbol = None
for v in valores:
    arbol = insertar(arbol, v)

print("Recorrido inorden:")
inorden(arbol)

print("\nRecorrido preorden:")
preorden(arbol)

print("\nRecorrido postorden:")
postorden(arbol)
