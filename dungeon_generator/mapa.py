
import random
from typing import Dict, Tuple, List
from habitacion import Habitacion

class Mapa:
    def __init__(self, ancho: int, alto: int):
        self.ancho = ancho
        self.alto = alto
        self.habitaciones: Dict[Tuple[int, int], Habitacion] = {}
        self.habitacion_inicial: Optional[Habitacion] = None 
        self._id_counter = 0
    
    def _generar_id(self) -> int:
        self._id_counter += 1
        return self._id_counter