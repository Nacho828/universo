
import math
from Estrella import Estrella


def calcular_distancia(self, otra_estrella):
        return math.sqrt(
            (self.x - otra_estrella.x) ** 2 +
            (self.y - otra_estrella.y) ** 2 +
            (self.z - otra_estrella.z) ** 2
        )

def distancia_al_origen(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

# Métodos adicionales
def contar_estrellas(estrellas):
    return len(estrellas)

def estrella_mas_lejana_al_origen(estrellas):
    return max(estrellas, key=lambda estrella: estrella.distancia_al_origen())

def crear_estrellas():
    estrella_a = Estrella("A", 2, 3, 1)
    estrella_b = Estrella("B", 4, 4, 4)
    estrella_c = Estrella("C", -3, -1, 0)
    return [estrella_a, estrella_b, estrella_c]

# Crear estrellas e imprimirlas
estrellas = crear_estrellas()
for estrella in estrellas:
    print(f"Estrella {estrella.nombre}: ({estrella.x}, {estrella.y}, {estrella.z})")

# Ejemplo de uso
estrella1 = Estrella("Estrella A", 0, 0, 0)
estrella2 = Estrella("Estrella B", 3, 4, 0)

distancia = estrella1.calcular_distancia(estrella2)
print(f"La distancia entre {estrella1.nombre} y {estrella2.nombre} es {distancia}")

# Contar estrellas
print(f"Total de estrellas: {contar_estrellas(estrellas)}")

# Estrella más lejana al origen
mas_lejana = estrella_mas_lejana_al_origen(estrellas)
print(f"La estrella más lejana al origen es {mas_lejana.nombre} con una distancia de {mas_lejana.distancia_al_origen()}")