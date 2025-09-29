import random
from abc import ABC, abstractmethod
from typing import Optional
from .objeto import Objeto

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
    
    @abstractmethod
    def to_dict(self) -> dict:
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
        return f"¡Encontraste {self.recompensa.nombre}! ({self.recompensa.descripcion})"
    
    def to_dict(self) -> dict:
        return {
            "tipo": "tesoro",
            "recompensa": self.recompensa.to_dict()
        }

class Monstruo(ContenidoHabitacion):
    def __init__(self, nombre: str, vida: int, ataque: int):
        self.nombre = nombre
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
    
    @property
    def descripcion(self) -> str:
        return f"Un {self.nombre} con {self.vida} de vida"
    
    @property
    def tipo(self) -> str:
        return "monstruo"
    
    def interactuar(self, explorador) -> str:
        mensaje = f"¡Te enfrentas a un {self.nombre}!\n"
        
        while self.vida > 0 and explorador.esta_vivo:
            # Turno del jugador
            if random.random() < 0.6:
                danio_jugador = random.randint(1, 2)
                self.vida -= danio_jugador
                mensaje += f"¡Golpeas al {self.nombre} por {danio_jugador} de daño! "
            else:
                mensaje += "Fallaste tu ataque. "
            
            if self.vida <= 0:
                mensaje += f"\n¡Derrotaste al {self.nombre}!"
                break
            
            # Turno del monstruo
            if random.random() < 0.7:
                explorador.recibir_dano(self.ataque)
                mensaje += f"El {self.nombre} te ataca por {self.ataque} de daño."
            else:
                mensaje += f"El {self.nombre} falla su ataque."
            
            mensaje += f" (Vida del {self.nombre}: {max(0, self.vida)})\n"
        
        if not explorador.esta_vivo:
            mensaje += f"\n¡Has sido derrotado por el {self.nombre}!"
        
        return mensaje
    
    def to_dict(self) -> dict:
        return {
            "tipo": "monstruo",
            "nombre": self.nombre,
            "vida": self.vida,
            "vida_maxima": self.vida_maxima,
            "ataque": self.ataque
        }

class Jefe(Monstruo):
    def __init__(self, nombre: str, vida: int, ataque: int, recompensa_especial: Objeto):
        super().__init__(nombre, vida, ataque)
        self.recompensa_especial = recompensa_especial
    
    @property
    def tipo(self) -> str:
        return "jefe"
    
    def interactuar(self, explorador) -> str:
        mensaje = f"¡CUIDADO! Te enfrentas al JEFE {self.nombre}!\n"
        
        while self.vida > 0 and explorador.esta_vivo:
            # Turno del jugador (menor probabilidad contra jefe)
            if random.random() < 0.4:
                danio_jugador = random.randint(1, 2)
                self.vida -= danio_jugador
                mensaje += f"¡Logras herir al {self.nombre} por {danio_jugador} de daño! "
            else:
                mensaje += "Tu ataque es esquivado. "
            
            if self.vida <= 0:
                explorador.inventario.append(self.recompensa_especial)
                mensaje += f"\n¡INCREIBLE! Derrotaste al JEFE {self.nombre}!"
                mensaje += f"\n¡Obtienes {self.recompensa_especial.nombre}!"
                break
            
            # Turno del jefe (mayor probabilidad)
            if random.random() < 0.8:
                explorador.recibir_dano(self.ataque)
                mensaje += f"El {self.nombre} te golpea por {self.ataque} de daño."
            else:
                mensaje += f"El {self.nombre} falla su ataque."
            
            mensaje += f" (Vida del {self.nombre}: {max(0, self.vida)})\n"
        
        if not explorador.esta_vivo:
            mensaje += f"\n¡El JEFE {self.nombre} te ha derrotado!"
        
        return mensaje
    
    def to_dict(self) -> dict:
        datos = super().to_dict()
        datos["tipo"] = "jefe"
        datos["recompensa_especial"] = self.recompensa_especial.to_dict()
        return datos
