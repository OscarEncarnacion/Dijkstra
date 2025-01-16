class Nodo:
    def __init__(self, identificador):
        self.id = identificador
        self.nodosAdyacentes = []
        self.visitado = False
        self.nodoAnterior = None
        self.distancia = float('inf')

    def agregarNodoAdyacente(self, nodo, costo):
        if nodo not in self.nodosAdyacentes:
            self.nodosAdyacentes.append([nodo, costo])


class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregarNodo(self, id):
        if id not in self.nodos:
            self.nodos[id] = Nodo(id)

    def agregarArista(self, nodoUno,nodoDos, costo):
        if nodoUno in self.nodos and nodoDos in self.nodos:
            self.nodos[nodoUno].agregarNodoAdyacente(nodoDos, costo)
            self.nodos[nodoDos].agregarNodoAdyacente(nodoUno, costo)

    def menorCosto(self, listaNodos):
        if len(listaNodos) > 0:
            costo = self.nodos[listaNodos[0]].distancia
            nodo = listaNodos[0]
            for elemento in listaNodos:
                if costo > self.nodos[elemento].distancia:
                    costo = self.nodos[elemento].distancia
                    nodo = elemento
            return nodo

    def ejecutarDijkstra(self, nodoInicial):
        if nodoInicial in self.nodos:
            self.nodos[nodoInicial].distancia = 0
            nodoActual = nodoInicial
            nodosNoVisitados = []
            for nodo in self.nodos:
                if nodo != nodoInicial:
                    self.nodos[nodo].distancia = float('inf')
                self.nodos[nodo].nodoAnterior = None
                nodosNoVisitados.append(nodo)
            while len(nodosNoVisitados) > 0:
                for adyacente in self.nodos[nodoActual].nodosAdyacentes:
                    if self.nodos[adyacente[0]].visitado == False:
                        if self.nodos[nodoActual].distancia + adyacente[1] < self.nodos[adyacente[0]].distancia:
                            self.nodos[adyacente[0]].distancia = self.nodos[nodoActual].distancia + adyacente[1]
                            self.nodos[adyacente[0]].nodoAnterior = nodoActual
                self.nodos[nodoActual].visitado = True
                nodosNoVisitados.remove(nodoActual)
                nodoActual = self.menorCosto(nodosNoVisitados)
        else:
            return False

    def imprimirGrafo(self):
        for nodo in self.nodos:
            print(f"El costo para llegar al nodo {str(nodo)} es de {str(self.nodos[nodo].distancia)} llegando desde el nodo {str(self.nodos[nodo].nodoAnterior)}")

    def ruta(self, nodoFinal):
        ruta = []
        nodoActual = nodoFinal
        while nodoActual != None:
            ruta.insert(0, nodoActual)
            nodoActual = self.nodos[nodoActual].nodoAnterior
        return f"El camino a seguir es: {ruta}\nEl costo es: {self.nodos[nodoFinal].distancia}"

def main():
    grafo = Grafo()
    #nodos = ['O', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'T']
    #aristas = [['O', 'C', 7], ['O', 'B', 7], ['O', 'A', 6], ['C', 'B', 1], ['C', 'E', 3], ['B', 'E', 4], ['B', 'D', 3], ['B', 'A', 2], ['A', 'D', 4], ['E', 'F', 5], ['E', 'G', 9], ['E', 'D', 3], ['D', 'G', 6], ['D', 'H', 4], ['F', 'T', 6], ['F', 'G', 2], ['G', 'T', 7], ['G', 'H', 1], ['H', 'T', 6]]
    nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    aristas = [['A', 'B', 3], ['A', 'C', 8], ['A', 'D', 5], ['B', 'F', 7], ['B', 'C', 5], ['C', 'F', 5], ['C', 'E', 8], ['C', 'D', 2], ['D', 'G', 4], ['F', 'H', 6], ['F', 'E', 5], ['E', 'H', 1], ['E', 'I', 3], ['E', 'G', 6], ['G', 'I', 4], ['H', 'J', 2], ['I', 'J', 6]]
    for nodo in nodos:
        grafo.agregarNodo(nodo)
    for arista in aristas:
        grafo.agregarArista(arista[0], arista[1], arista[2])
    grafo.ejecutarDijkstra('A')
    print(grafo.ruta('J'))

if __name_ == '__main__':
    main()
