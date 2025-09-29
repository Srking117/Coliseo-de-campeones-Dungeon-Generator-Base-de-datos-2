from typing import Dict, Optional, Tuple
from abc import ABC, abstractmethod
from .objeto import Objeto

class ContenidoHabitacion(ABC):
    @property
    @abstractmethod
    def descripcion(self) -> str:
        raise NotImplementedError
    
    @property
    @abstractmethod
    def tipo(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def interactuar(self, explorador) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def to_dict(self) -> dict:
        """Convierte el contenido a diccionario para serializacion"""
        raise NotImplementedError

class Habitacion:
    def __init__(self, id: int, x: int, y: int, inicial: bool = False):
        self.id = id
        self.x = x
        self.y = y
        self.inicial = inicial
        self.contenido: Optional[ContenidoHabitacion] = None
        self.conexiones: Dict[str, 'Habitacion'] = {}
        self.visitada = False
    
    def agregar_conexion(self, direccion: str, habitacion: 'Habitacion'):
        self.conexiones[direccion] = habitacion
    
    def obtener_direcciones_disponibles(self) -> list[str]:
        return list(self.conexiones.keys())
    
    def __str__(self) -> str:
        estado = "inicial" if self.inicial else "normal"
        visitada = "visitada" if self.visitada else "no visitada"
        contenido = self.contenido.tipo if self.contenido else "vacía"
        return f"Habitacion {self.id} ({self.x},{self.y}) - {estado} - {visitada} - {contenido}"
    
    def to_dict(self) -> dict:
        """Convierte la habitacion a diccionario para serializacion"""
        datos = {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "inicial": self.inicial,
            "visitada": self.visitada,
            "contenido": None
        }
        
        if self.contenido:
            datos["contenido"] = self.contenido.to_dict()
        
        return datos
