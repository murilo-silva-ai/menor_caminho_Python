# Utilizado o método de bellman ford

def bellman_ford(grafo, inicio, fim):
    distancia = {vertice: float('infinity') for vertice in grafo}
    predecessor = {vertice: None for vertice in grafo}
    distancia[inicio] = 0

    for _ in range(len(grafo) - 1):
        for u in grafo:
            for v in grafo[u]:
                if distancia[u] + grafo[u][v] < distancia[v]:
                    distancia[v] = distancia[u] + grafo[u][v]
                    predecessor[v] = u

    for u in grafo:
        for v in grafo[u]:
            if distancia[u] + grafo[u][v] < distancia[v]:
                raise ValueError("O grafo contém um ciclo de peso negativo")

    caminho = []
    vertice_atual = fim
    while vertice_atual is not None:
        caminho.append(vertice_atual)
        vertice_atual = predecessor[vertice_atual]
    caminho = caminho[::-1]  # Reverter o caminho

    return caminho, distancia[fim]

grafo = {
    "1": {"2": 3.35, "5": 0.83, "6": 2.3, "7": 0.7},
    "2": {"1": 3.35, "16": 2.7, "21": 4},
    "3": {"10": 2.9, "17": 9.35},
    "4": {"7": 2.85, "11": 2.3, "19": 3, "23": 1.75},
    "5": {"1": 0.85, "9": 1.9, "10": 3.5},
    "6": {"1": 2.3, "8": 1.8},
    "7": {"1": 0.7, "4": 2.85, "23": 2.65},
    "8": {"6": 1.8, "13": 3.55},
    "9": {"5": 1.9, "14": 7.7, "17": 3.4, "18": 2.5},
    "10": {"3": 2.9, "5": 3.5, "13": 4.65, "17": 4.3},
    "11": {"4": 2.3, "12": 3.25},
    "12": {"11": 3.25, "13": 1.6},
    "13": {"8": 3.55, "10": 4.65, "12": 1.6, "23": 7.1},
    "14": {"9": 7.7, "15": 3.9, "21": 7.65},
    "15": {"14": 3.9},
    "16": {"2": 2.7, "19": 6.75, "20": 5.2},
    "17": {"3": 9.35, "9": 3.4, "10": 4.3, "18": 4.15},
    "18": {"9": 2.5, "17": 4.15, "21": 2.5, "23": 6.4},
    "19": {"4": 3, "16": 6.75},
    "20": {"16": 5.2, "21": 3.55, "22": 6.54},
    "21": {"2": 4, "14": 7.65, "18": 2.5, "20": 3.55},
    "22": {"20": 6.54},
    "23": {"4": 1.75, "7": 2.65, "13": 7.1, "18": 6.4}
}

vertice_inicial = "3"
vertice_final = "22"

caminho, custo = bellman_ford(grafo, vertice_inicial, vertice_final)
custo = round(custo, 2)
print(f"Menor caminho de {vertice_inicial} para {vertice_final}: {' -> '.join(caminho)} com custo total de {custo}")
