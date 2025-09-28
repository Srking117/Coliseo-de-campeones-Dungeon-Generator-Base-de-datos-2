from typing import Dict, Optional, Tuple
from .objeto import Objeto


class ContenidoHabitacion:
   
    
    @property
    def descripcion(self) -> str:
        raise NotImplementedError
    
    @property
    def tipo(self) -> str:
        raise NotImplementedError
    
    def interactuar(self, explorador) -> str:
        raise NotImplementedError


class Habitacion:
    
    
    def __init__(self, id: int, x: int, y: int, inicial: bool = False):
        self.id = id
        self.x = x
        self.y = y
        self.inicial = inicial
        self.contenido: Optional[ContenidoHabitacion] = None
        self.conexiones: Dict[str, 'Habitacion'] = {}  # 4 puntos cardinales: norte, sur, este, oeste
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
           
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "inicial": self.inicial,
            "visitada": self.visitada,
            
        }