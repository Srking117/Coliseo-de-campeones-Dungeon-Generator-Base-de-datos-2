"""Sebastian Riveros Koenderink - Base de datos 2 - Umag"""

from dungeon_generator.mapa import Mapa
from dungeon_generator.explorador import Explorador
from dungeon_generator.objeto import Objeto
from dungeon_generator.contenido import Tesoro, Monstruo, Jefe
from dungeon_generator.serializador import Serializador

def main():
    print("=== 🏛️ Coliseo de campeones 🏛️ ===\n")
  

    objetos_tesoro = [
        Objeto("Aguijon", 100, "De tierras lejanas, pertenecio a un caballero llamado Hollow Knight"),
        Objeto(" 🏺 Frasco de Estus 🏺", 25, "Restaura 2 puntos de vida - Proviene de un mundo, ya un reino olvidado protegido por el Dark Souls"),
        Objeto("Sombrero de Artur Morgan", 75, "Pertenecio a un lengendario forajido del lejano oeste, este sombrero te otorgara honor, y velocidad de disparo"),
        Objeto("Pokebola", 150, "Se desconoce su origen, pero se dice que contiene a Pikachu..."),
    ]
    
    
    objetos_jefe = [
        Objeto("Guantelete del Infinito", 200, "Contiene las 6 gemas del infinito, con el poder de destruir la mitad del universo"),
        Objeto("Espadas del Caos", 180, "Pertenecientes al dios de la guerra Kratos"),
        Objeto("Sombrero de Teemo", 220, "Si ese sombrero... el de League of Legends..."),
    ]
    
    print("Objetos de tesoro creados:")
    for obj in objetos_tesoro:
        print(f"- {obj}")
    print()
    
    print("Objetos de jefe creados:")
    for obj in objetos_jefe:
        print(f"- {obj}")
    print()
    
    
    mapa = Mapa(ancho=6, alto=6)
    mapa.generar_estructura(n_habitaciones=15)
    
    print(f"Mapa generado: {mapa.ancho}x{mapa.alto}")
    print(f"Habitaciones creadas: {len(mapa.habitaciones)}")
    print(f"Habitación inicial: ({mapa.habitacion_inicial.x}, {mapa.habitacion_inicial.y})")
    print()
    
    
    mapa.colocar_contenido(objetos_tesoro, objetos_jefe)
    print("Contenido colocado automaticamente en el mapa")
    print()
    
    
    stats = mapa.obtener_estadisticas_mapa()
    print("=== ESTADÍSTICAS DEL MAPA ===")
    print(f"Total habitaciones: {stats['total_habitaciones']}")
    print(f"Promedio conexiones: {stats['promedio_conexiones']}")
    print("Distribución de contenido:")
    for tipo, cantidad in stats['distribucion_contenido'].items():
        print(f"  - {tipo}: {cantidad}")
    print()
    

    explorador = Explorador(mapa)
    
    print("Explorador Noble Six creado:")
    print(explorador.obtener_estadisticas())
    print(f"Posicion actual: {explorador.posicion_actual}")
    print()
    
   
    print("Direcciones disponibles:", explorador.obtener_habitaciones_adyacentes())
    print()
    

    print("Explorando habitacion actual...")
    resultado = explorador.explorar_habitacion()
    print(resultado)
    print()
    
   
    print("=== GUARDANDO PARTIDA ===")
    Serializador.guardar_partida(mapa, explorador, "partida_guardada.json")
    print()
    

    print("=== ESTADO FINAL ===")
    print(explorador.obtener_estadisticas())
    print(f"Inventario: {[obj.nombre for obj in explorador.inventario]}")
    print(f"¿Sigue vivo?: {'Sí' if explorador.esta_vivo else 'No'}")
    print()
    
    print("¡Aventurate en el coliseo de campeones!")

if __name__ == "__main__":
    main()
