"""
LEGALI BRAIN

Clase base para todos los Directores IA.

Ningún Director debe implementarse desde cero.

Todos heredarán de BaseDirector.

Autor:
LEGALI BRAIN v2.0
"""

from abc import ABC, abstractmethod
from datetime import datetime


class BaseDirector(ABC):

    def __init__(self, nombre: str):

        self.nombre = nombre
        self.fecha_inicio = datetime.now()

        self.objetivo = None
        self.analisis = {}
        self.decision = None

    @abstractmethod
    def analizar(self):
        """
        Analiza la información disponible.
        """
        pass

    @abstractmethod
    def decidir(self):
        """
        Toma una decisión.
        """
        pass

    def ejecutar(self):

        print()
        print("=" * 60)
        print(f"🧠 {self.nombre}")
        print("=" * 60)

        self.analizar()

        self.decision = self.decidir()

        return self.decision