import random
from typing import Dict, Tuple, List, Optional
from .habitacion import Habitacion

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
    
    def _posicion_valida(self, x: int, y: int) -> bool:
       
        return 0 <= x < self.ancho and 0 <= y < self.alto
    
    def _es_borde(self, x: int, y: int) -> bool:
        
        return x == 0 or x == self.ancho - 1 or y == 0 or y == self.alto - 1
    
    def _obtener_direccion_opuesta(self, direccion: str) -> str:
       
        opuestas = {'norte': 'sur', 'sur': 'norte', 'este': 'oeste', 'oeste': 'este'}
        return opuestas[direccion]
    
    def _obtener_coordenada_vecina(self, x: int, y: int, direccion: str) -> Tuple[int, int]:
        
        movimientos = {'norte': (0, -1), 'sur': (0, 1), 'este': (1, 0), 'oeste': (-1, 0)}
        dx, dy = movimientos[direccion]
        return x + dx, y + dy
    
    def generar_estructura(self, n_habitaciones: int) -> None:
       
        
       
        max_habitaciones = self.ancho * self.alto
        if n_habitaciones > max_habitaciones:
            raise ValueError(f"No se pueden generar {n_habitaciones} habitaciones en un mapa de {self.ancho}x{self.alto}")
        

        posiciones_borde = []
        for x in range(self.ancho):
            for y in range(self.alto):
                if self._es_borde(x, y):
                    posiciones_borde.append((x, y))
        
        x_inicial, y_inicial = random.choice(posiciones_borde)
        habitacion_inicial = Habitacion(self._generar_id(), x_inicial, y_inicial, inicial=True)
        self.habitaciones[(x_inicial, y_inicial)] = habitacion_inicial
        self.habitacion_inicial = habitacion_inicial
        
        
        habitaciones_generadas = 1
        x_actual, y_actual = x_inicial, y_inicial
        direcciones = ['norte', 'sur', 'este', 'oeste']
        
        while habitaciones_generadas < n_habitaciones:
          
            random.shuffle(direcciones)
            movimiento_exitoso = False
            
            for direccion in direcciones:
                x_nuevo, y_nuevo = self._obtener_coordenada_vecina(x_actual, y_actual, direccion)
                
                
                if (self._posicion_valida(x_nuevo, y_nuevo) and 
                    (x_nuevo, y_nuevo) not in self.habitaciones):
                    
                    
                    nueva_habitacion = Habitacion(self._generar_id(), x_nuevo, y_nuevo)
                    self.habitaciones[(x_nuevo, y_nuevo)] = nueva_habitacion
                    
                  
                    habitacion_actual = self.habitaciones[(x_actual, y_actual)]
                    habitacion_actual.agregar_conexion(direccion, nueva_habitacion)
                    nueva_habitacion.agregar_conexion(self._obtener_direccion_opuesta(direccion), habitacion_actual)
                    
                    x_actual, y_actual = x_nuevo, y_nuevo
                    habitaciones_generadas += 1
                    movimiento_exitoso = True
                    break
            
            
            if not movimiento_exitoso and habitaciones_generadas < n_habitaciones:
                posicion_aleatoria = random.choice(list(self.habitaciones.keys()))
                x_actual, y_actual = posicion_aleatoria
    
    def obtener_habitacion_por_coordenadas(self, x: int, y: int) -> Optional[Habitacion]:
       
        return self.habitaciones.get((x, y))
