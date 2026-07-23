from abc import ABC, abstractmethod

class BaseProvider(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def generar_imagen(self, prompt):
        """Genera una imagen y devuelve la ruta del archivo."""
        pass

    @abstractmethod
    def generar_texto(self, prompt):
        """Genera texto y devuelve una cadena."""
        pass