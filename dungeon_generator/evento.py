import random
from .contenido import ContenidoHabitacion
from .objeto import Objeto

class Evento(ContenidoHabitacion):
    """Eventos especiales del Coliseo de Campeones"""
    
    def __init__(self, nombre: str, descripcion: str, efecto: str):
        self._nombre = nombre
        self._descripcion = descripcion
        self.efecto = efecto
        self.duracion = 0
    
    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @property
    def tipo(self) -> str:
        return "evento"
    
    def interactuar(self, explorador) -> str:
        if self.efecto == "curacion":
            curacion = random.randint(1, 3)
            explorador.curar(curacion)
            return f"¡{self._nombre}! Recuperas {curacion} puntos de vida."
        
        elif self.efecto == "trampa":
            danio = random.randint(1, 2)
            explorador.recibir_dano(danio)
            return f"¡{self._nombre}! Pierdes {danio} puntos de vida."
        
        elif self.efecto == "portal":
            # Teletransportar a habitación aleatoria
            habitaciones = list(explorador.mapa.habitaciones.values())
            nueva_habitacion = random.choice(habitaciones)
            explorador.posicion_actual = (nueva_habitacion.x, nueva_habitacion.y)
            return f"¡{self._nombre}! Teletransportado a ({nueva_habitacion.x}, {nueva_habitacion.y})"
        
        elif self.efecto == "bonificacion":
            explorador.bonificacion_combate = 3  # Para las próximas 3 habitaciones
            return f"¡{self._nombre}! Bonificación de combate por 3 habitaciones."
        
        return f"¡{self._nombre}! No tiene efecto aparente."
    
    def to_dict(self) -> dict:
        return {
            "tipo": "evento",
            "nombre": self._nombre,
            "descripcion": self._descripcion,
            "efecto": self.efecto
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Evento':
        return cls(
            nombre=data["nombre"],
            descripcion=data["descripcion"],
            efecto=data["efecto"]
        )

# Eventos específicos del Coliseo
class GritoMultitud(Evento):
    """La multitud anima al gladiador"""
    def __init__(self):
        super().__init__(
            "Grito de la Multitud",
            "El público corea tu nombre, te sientes inspirado",
            "bonificacion"
        )

class TrampaGladiadores(Evento):
    """Trampa antigua del coliseo"""
    def __init__(self):
        super().__init__(
            "Trampa de Gladiadores",
            "Pisaste una trampa oculta en la arena",
            "trampa"
        )

class FuenteCampeones(Evento):
    """Fuente que restaura vida"""
    def __init__(self):
        super().__init__(
            "Fuente de los Campeones",
            "Agua bendita que cura las heridas",
            "curacion"
        )

class PortalDestino(Evento):
    """Portal mágico del coliseo"""
    def __init__(self):
        super().__init__(
            "Portal del Destino",
            "Un portal te transporta a otra parte del coliseo",
            "portal"
        )

class FantasmaCampeon(Evento):
    """Fantasma que ayuda en combate"""
    def __init__(self):
        super().__init__(
            "Alma de Campeón de las cenizas pasado",
            "El espíritu de un antiguo campeón te otorga su bendición",
            "bonificacion"
        )
