import random
from typing import Dict, Tuple, List, Optional
from .habitacion import Habitacion
from .contenido import Tesoro, Monstruo, Jefe
from .objeto import Objeto

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
    
    def _calcular_distancia_manhattan(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """Calcula la distancia Manhattan entre dos puntos"""
        return abs(x1 - x2) + abs(y1 - y2)
    
    def generar_estructura(self, n_habitaciones: int) -> None:
        max_habitaciones = self.ancho * self.alto
        if n_habitaciones > max_habitaciones:
            raise ValueError(f"No se pueden generar {n_habitaciones} habitaciones en un mapa de {self.ancho}x{self.alto}")
        
        # Generar habitación inicial en el borde
        posiciones_borde = []
        for x in range(self.ancho):
            for y in range(self.alto):
                if self._es_borde(x, y):
                    posiciones_borde.append((x, y))
        
        x_inicial, y_inicial = random.choice(posiciones_borde)
        habitacion_inicial = Habitacion(self._generar_id(), x_inicial, y_inicial, inicial=True)
        self.habitaciones[(x_inicial, y_inicial)] = habitacion_inicial
        self.habitacion_inicial = habitacion_inicial
        
        # Generar habitaciones adicionales
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
    
    def colocar_contenido(self, objetos_tesoro: List[Objeto], objetos_jefe: List[Objeto]) -> None:
        """Coloca contenido en las habitaciones incluyendo eventos"""
        
        habitaciones_disponibles = [
            habitacion for habitacion in self.habitaciones.values() 
            if not habitacion.inicial
        ]
        
        if not habitaciones_disponibles:
            return
        
        total_habitaciones = len(habitaciones_disponibles)
        
        # Colocar jefe 
        jefe_habitacion = random.choice(habitaciones_disponibles)
        objeto_jefe = random.choice(objetos_jefe)
        distancia_jefe = self._calcular_distancia_manhattan(
            jefe_habitacion.x, jefe_habitacion.y,
            self.habitacion_inicial.x, self.habitacion_inicial.y
        )
        vida_jefe = 6 + distancia_jefe  # Jefe mas fuerte segun distancia
        ataque_jefe = 2 + (distancia_jefe // 2)  # Ataque escala con distancia
        
        jefe_habitacion.contenido = Jefe(
            f"Jefe Final Nv.{distancia_jefe}", 
            vida_jefe, 
            ataque_jefe, 
            objeto_jefe
        )
        habitaciones_disponibles.remove(jefe_habitacion)
        
        # Calcular cantidades con porcentajes
        n_monstruos = max(1, int(total_habitaciones * random.uniform(0.2, 0.3)))
        n_tesoros = max(1, int(total_habitaciones * random.uniform(0.15, 0.25)))
        n_eventos = max(1, int(total_habitaciones * random.uniform(0.05, 0.1)))
        
        # Colocar monstruos (20-30%)
        monstruos_colocados = 0
        while monstruos_colocados < n_monstruos and habitaciones_disponibles:
            habitacion = random.choice(habitaciones_disponibles)
            distancia = self._calcular_distancia_manhattan(
                habitacion.x, habitacion.y,
                self.habitacion_inicial.x, self.habitacion_inicial.y
            )
            
            # Monstruos mas fuertes segun distancia
            vida_monstruo = 3 + distancia
            ataque_monstruo = 1 + (distancia // 3)
            
            tipos_monstruos = ["Teemo", "Megatron", "Gengar", "Bowser", "Revolver Ocelot"]
            nombre_monstruo = f"{random.choice(tipos_monstruos)} Nv.{distancia}"
            
            habitacion.contenido = Monstruo(nombre_monstruo, vida_monstruo, ataque_monstruo)
            habitaciones_disponibles.remove(habitacion)
            monstruos_colocados += 1
        
        # Colocar tesoros (15-25%)
        tesoros_colocados = 0
        while tesoros_colocados < n_tesoros and habitaciones_disponibles and objetos_tesoro:
            habitacion = random.choice(habitaciones_disponibles)
            objeto_tesoro = random.choice(objetos_tesoro)
            
            # Tesoros mas valiosos segun distancia
            distancia = self._calcular_distancia_manhattan(
                habitacion.x, habitacion.y,
                self.habitacion_inicial.x, self.habitacion_inicial.y
            )
            objeto_tesoro.valor = objeto_tesoro.valor + (distancia * 10)  # Mas valor por distancia
            
            habitacion.contenido = Tesoro(objeto_tesoro)
            habitaciones_disponibles.remove(habitacion)
            tesoros_colocados += 1
        
        # Colocar eventos (5-10%)
        from .eventos import GritoMultitud, TrampaGladiadores, FuenteCampeones, PortalDestino, FantasmaCampeon
        eventos_disponibles = [GritoMultitud, TrampaGladiadores, FuenteCampeones, PortalDestino, FantasmaCampeon]
        
        eventos_colocados = 0
        while eventos_colocados < n_eventos and habitaciones_disponibles:
            habitacion = random.choice(habitaciones_disponibles)
            evento_clase = random.choice(eventos_disponibles)
            habitacion.contenido = evento_clase()
            habitaciones_disponibles.remove(habitacion)
            eventos_colocados += 1
        
        # El resto de habitaciones quedan vacias
    
    def obtener_estadisticas_mapa(self) -> Dict[str, int | float]:
        """Obtiene estadísticas del mapa"""
        total_habitaciones = len(self.habitaciones)
        
        # Contar contenido
        contenido_stats = {
            "inicial": 0,
            "vacia": 0,
            "tesoro": 0,
            "monstruo": 0,
            "jefe": 0,
            "evento": 0
        }
        
        total_conexiones = 0
        
        for habitacion in self.habitaciones.values():
            if habitacion.inicial:
                contenido_stats["inicial"] += 1
            elif habitacion.contenido:
                contenido_stats[habitacion.contenido.tipo] += 1
            else:
                contenido_stats["vacia"] += 1
            
            total_conexiones += len(habitacion.conexiones)
        
        promedio_conexiones = total_conexiones / total_habitaciones if total_habitaciones > 0 else 0
        
        return {
            "total_habitaciones": total_habitaciones,
            "distribucion_contenido": contenido_stats,
            "promedio_conexiones": round(promedio_conexiones, 2)
        }
    
    def obtener_habitacion_por_coordenadas(self, x: int, y: int) -> Optional[Habitacion]:
        return self.habitaciones.get((x, y))
    
    def to_dict(self) -> Dict:
        """Convierte el mapa a diccionario para serializacion"""
        return {
            "ancho": self.ancho,
            "alto": self.alto,
            "habitaciones": {
                f"{x},{y}": habitacion.to_dict() 
                for (x, y), habitacion in self.habitaciones.items()
            },
            "habitacion_inicial": f"{self.habitacion_inicial.x},{self.habitacion_inicial.y}",
            "_id_counter": self._id_counter
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Mapa':
        """Crea un mapa desde un diccionario"""
        mapa = cls(data["ancho"], data["alto"])
        mapa._id_counter = data["_id_counter"]
        
        # Primero crear todas las habitaciones
        for coord_str, habitacion_data in data["habitaciones"].items():
            x, y = map(int, coord_str.split(','))
            habitacion = Habitacion(
                habitacion_data["id"],
                x, y,
                habitacion_data["inicial"]
            )
            habitacion.visitada = habitacion_data["visitada"]
            
            # Reconstruir contenido si existe
            if habitacion_data["contenido"]:
                contenido_data = habitacion_data["contenido"]
                tipo_contenido = contenido_data["tipo"]
                
                if tipo_contenido == "tesoro":
                    from .contenido import Tesoro
                    habitacion.contenido = Tesoro.from_dict(contenido_data)
                elif tipo_contenido == "monstruo":
                    from .contenido import Monstruo
                    habitacion.contenido = Monstruo.from_dict(contenido_data)
                elif tipo_contenido == "jefe":
                    from .contenido import Jefe
                    habitacion.contenido = Jefe.from_dict(contenido_data)
                elif tipo_contenido == "evento":
                    from .eventos import Evento
                    habitacion.contenido = Evento.from_dict(contenido_data)
            
            mapa.habitaciones[(x, y)] = habitacion
            
            if habitacion.inicial:
                mapa.habitacion_inicial = habitacion
        
        # Ahora reconstruir conexiones
        for coord_str, habitacion_data in data["habitaciones"].items():
            x, y = map(int, coord_str.split(','))
            habitacion_actual = mapa.habitaciones[(x, y)]
            
            # Reconstruir conexiones buscando habitaciones vecinas
            direcciones = ['norte', 'sur', 'este', 'oeste']
            for direccion in direcciones:
                x_vec, y_vec = mapa._obtener_coordenada_vecina(x, y, direccion)
                if (x_vec, y_vec) in mapa.habitaciones:
                    habitacion_vecina = mapa.habitaciones[(x_vec, y_vec)]
                    habitacion_actual.agregar_conexion(direccion, habitacion_vecina)
        
        return mapa
