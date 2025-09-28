from typing import List, Optional
from .objeto import Objeto
from .mapa import Mapa

class Explorador:
    def __init__(self, mapa: Mapa):
        self.vida: int = 5
        self.vida_maxima: int = 5
        self.inventario: List[Objeto] = []
        self.mapa: Mapa = mapa
        self.posicion_actual: Tuple[int, int] = mapa.habitacion_inicial.x, mapa.habitacion_inicial.y
    
    def mover(self, direccion: str) -> bool:
        
        direccion = direccion.lower()
        direcciones_validas = ['norte', 'sur', 'este', 'oeste']
        
        if direccion not in direcciones_validas:
            print(f"Direccion '{direccion}' no valida. Use: {direcciones_validas}")
            return False
        
        habitacion_actual = self.mapa.obtener_habitacion_por_coordenadas(*self.posicion_actual)
        
        if direccion in habitacion_actual.conexiones:
            habitacion_destino = habitacion_actual.conexiones[direccion]
            self.posicion_actual = (habitacion_destino.x, habitacion_destino.y)
            print(f"Te moviste al {direccion} hacia la habitacion ({habitacion_destino.x}, {habitacion_destino.y})")
            return True
        else:
            print(f"No hay conexion hacia el {direccion}")
            return False
    
    def explorar_habitacion(self) -> str:
       
        habitacion_actual = self.mapa.obtener_habitacion_por_coordenadas(*self.posicion_actual)
        habitacion_actual.visitada = True
        
        if habitacion_actual.contenido is None:
            return "La habitacion está vacia."
        else:
            resultado = habitacion_actual.contenido.interactuar(self)
            habitacion_actual.contenido = None  
            return resultado
    
    def obtener_habitaciones_adyacentes(self) -> List[str]:
        
        habitacion_actual = self.mapa.obtener_habitacion_por_coordenadas(*self.posicion_actual)
        return list(habitacion_actual.conexiones.keys())
    
    def recibir_dano(self, cantidad: int) -> None:
        
        self.vida = max(0, self.vida - cantidad)
        print(f"¡Recibiste {cantidad} de daño! Vida restante: {self.vida}")
    
    def curar(self, cantidad: int) -> None:
        """Cura al explorador"""
        self.vida = min(self.vida_maxima, self.vida + cantidad)
        print(f"¡Recuperaste {cantidad} de vida! Vida actual: {self.vida}")
    
    @property
    def esta_vivo(self) -> bool:
        """Verifica si el explorador tiene vida restante"""
        return self.vida > 0
    
    def obtener_estadisticas(self) -> str:
        """Devuelve estadisticas del explorador"""
        return f"Vida: {self.vida}/{self.vida_maxima} | Inventario: {len(self.inventario)} objetos"