"""Sebastian Riveros Koenderink - Base de datos 2 - Umag"""

from dungeon_generator.mapa import Mapa
from dungeon_generator.explorador import Explorador
from dungeon_generator.objeto import Objeto
from dungeon_generator.contenido import Tesoro, Monstruo, Jefe

def main():
    print("=== Coliseo de campeones ===\n")
    
    # Crear objetos
    aguijon = Objeto("Aguijon", 100, "De tierras lejanas, pertenecio a un caballero llamado Hollow Knight")
    pocion_vida = Objeto("Frasco de Estus", 25, "Restaura 2 puntos de vida - Proviene de un mundo, ya un reino olvidado protegido por el Dark Souls") 
    Guantelete_del_Infinito = Objeto("Guantelete del Infinito", 200, "Contiene las 6 gemas del infinito, con el poder de destruir la mitad del universo ")
    
    print("Objetos creados:")
    print(f"- {aguijon}")
    print(f"- {pocion_vida}")
    print(f"- {Guantelete_del_Infinito}")
    print()
    
    # Crear mapa y generar estructura
    mapa = Mapa(ancho=5, alto=5)
    mapa.generar_estructura(n_habitaciones=10)
    
    print(f"Mapa generado: {mapa.ancho}x{mapa.alto}")
    print(f"Habitaciones creadas: {len(mapa.habitaciones)}")
    print(f"Habitacion inicial: ({mapa.habitacion_inicial.x}, {mapa.habitacion_inicial.y})")
    print()
    
    # Colocar contenido de prueba
    habitacion1 = mapa.obtener_habitacion_por_coordenadas(1, 1)
    if habitacion1:
        habitacion1.contenido = Tesoro(pocion_vida)
    
    habitacion2 = mapa.obtener_habitacion_por_coordenadas(2, 2)
    if habitacion2:
        habitacion2.contenido = Monstruo("Teemo", vida=3, ataque=1)
    
    habitacion3 = mapa.obtener_habitacion_por_coordenadas(3, 3)
    if habitacion3:
        habitacion3.contenido = Jefe("Megatron", vida=6, ataque=2, recompensa_especial=Guantelete_del_Infinito)
    
    # Crear explorador
    explorador = Explorador(mapa)
    
    print("Explorador Noble Six creado:")
    print(explorador.obtener_estadisticas())
    print(f"Posicion actual: {explorador.posicion_actual}")
    print()
    
    # Probar movimiento
    print("Direcciones disponibles:", explorador.obtener_habitaciones_adyacentes())
    print()
    
    # Probar exploración de habitación inicial
    print("Explorando habitacion actual...")
    resultado = explorador.explorar_habitacion()
    print(resultado)
    print()
    
    print("¡Aventurate en el coliseo de campeones!")

    

if __name__ == "__main__":
    main()

