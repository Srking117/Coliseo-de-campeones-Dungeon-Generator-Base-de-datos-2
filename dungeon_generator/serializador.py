import json
from typing import Dict, Any
from .mapa import Mapa
from .explorador import Explorador
from .objeto import Objeto

class Serializador:
    @staticmethod
    def guardar_partida(mapa: Mapa, explorador: Explorador, archivo: str) -> None:
        """Guarda el estado completo del mapa y explorador en JSON"""
        
        datos_partida = {
            "mapa": mapa.to_dict(),
            "explorador": {
                "vida": explorador.vida,
                "vida_maxima": explorador.vida_maxima,
                "inventario": [objeto.to_dict() for objeto in explorador.inventario],
                "posicion_actual": list(explorador.posicion_actual)
            }
        }
        
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos_partida, f, indent=2, ensure_ascii=False)
        
        print(f"Partida guardada en: {archivo}")
    # Reconstruye lo siguiente:
    @staticmethod
    def cargar_partida(archivo: str) -> tuple[Mapa, Explorador]:
        """Carga una partida completa desde archivo JSON"""
        
        with open(archivo, 'r', encoding='utf-8') as f:
            datos_partida = json.load(f)
        
        #  mapa
        mapa = Mapa.from_dict(datos_partida["mapa"])
        
        # explorador
        explorador = Explorador(mapa)
        explorador.vida = datos_partida["explorador"]["vida"]
        explorador.vida_maxima = datos_partida["explorador"]["vida_maxima"]
        
        # inventario
        explorador.inventario = [
            Objeto.from_dict(objeto_data) 
            for objeto_data in datos_partida["explorador"]["inventario"]
        ]
        
        # Establecer posición actual
        pos_data = datos_partida["explorador"]["posicion_actual"]
        explorador.posicion_actual = (pos_data[0], pos_data[1])
        
        print(f"Partida cargada desde: {archivo}")
        return mapa, explorador