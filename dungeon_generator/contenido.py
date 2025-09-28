
from abc import ABC, abstractmethod
from typing import Optional
from dungeon_generator.objeto import Objeto

class ContenidoHabitacion(ABC):
    @property
    @abstractmethod
    def descripcion(self) -> str:
        pass
    
    @property
    @abstractmethod
    def tipo(self) -> str:
        pass
    
    @abstractmethod
    def interactuar(self, explorador) -> str:
        pass

class Tesoro(ContenidoHabitacion):
    def __init__(self, recompensa: Objeto):
        self.recompensa = recompensa
    
    @property
    def descripcion(self) -> str:
        return f"Un cofre de almas que contiene {self.recompensa.nombre}"
    
    @property
    def tipo(self) -> str:
        return "tesoro"
    
    def interactuar(self, explorador) -> str:
        explorador.inventario.append(self.recompensa)
        return f"¡Encontraste {self.recompensa.nombre}!"