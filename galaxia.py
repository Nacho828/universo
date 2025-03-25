from Estrella import Estrellas  # Asegúrate de que Estrella esté definida en Estrellas.py

class Galaxia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estrellas = []

    def agregar_estrella(self, estrella):
        if isinstance(estrella, Estrellas):
            self.estrellas.append(estrella)
        else:
            raise TypeError("El objeto debe ser una instancia de la clase Estrella")

    def __str__(self):
        return f"Galaxia {self.nombre} con {len(self.estrellas)} estrellas"

    def name(self): 
        return self.nombre