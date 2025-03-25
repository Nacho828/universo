import math
    
def __str__(self):
        return f"Estrella({self.x}, {self.y}, {self.z})"

def galaxia(self):
        # Determina la galaxia basada en las coordenadas (ejemplo simple)
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Alfa"
        elif self.x < 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Beta"
        elif self.x < 0 and self.y < 0 and self.z >= 0:
            return "Galaxia Gamma"
        else:
            return "Galaxia Delta"

def distancia(self, otra_estrella):
        return math.sqrt(
            (self.x - otra_estrella.x) ** 2 +
            (self.y - otra_estrella.y) ** 2 +
            (self.z - otra_estrella.z) ** 2
        )

# Ejemplo de uso
estrella1 = Estrella(1, 2, 3)
estrella2 = Estrella(-1, -2, -3)

print(estrella1)  # Salida: Estrella(1, 2, 3)
print(estrella1.galaxia())  # Salida: Galaxia Alfa
print(estrella1.distancia(estrella2))  # Calcula la distancia entre estrella1 y estrella2