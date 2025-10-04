"""Sebastian Riveros Koenderink - Base de datos 2 - Umag"""

from dungeon_generator.mapa import Mapa
from dungeon_generator.explorador import Explorador
from dungeon_generator.objeto import Objeto
from dungeon_generator.contenido import Tesoro, Monstruo, Jefe
from dungeon_generator.serializador import Serializador
from dungeon_generator.visualizador import Visualizador
import random
import time

def mostrar_titulo():
    
    titulo = """
    ============================================================
              COLISEO DE CAMPEONES 
              LA LEYENDA DE NOBLE SIX
    ============================================================
        Bienvenido, gladiador! El destino te espera...
    ============================================================
    """
    print(titulo)

def main():
    mostrar_titulo()
    
    # Crear objetos de tesoro
    print("PREPARANDO LAS RELIQUIAS DEL COLISEO...")
    time.sleep(1)
    
    objetos_tesoro = [
        Objeto("Aguijón de Hollow Knight", 100, "Espada ancestral de un caballero de tierras lejanas"),
        Objeto("🏺 Frasco de Estus 🏺", 25, "Elixir que restaura la vitalidad del portador"),
        Objeto("Sombrero de Artur Morgan", 75, "Emblema de honor de un legendario forajido"),
        Objeto("Pokebola ", 150, "Se desconoce su origen, pero se dice que contiene a Pikachu..."),
    ]
    
    objetos_jefe = [
        Objeto("Guantelete del Infinito", 200, "Artefacto cósmico con poder sobre la realidad"),
        Objeto("Espadas del Caos", 180, "Armas divinas del Dios de la Guerra"),
        Objeto("Sombrero de Teemo", 220, "Reliquia de poder misterioso y temido"),
    ]
    
    print("Reliquias preparadas para la batalla!\n")
    time.sleep(1)
    
    # Crear y generar mapa
    print("CONSTRUYENDO EL GRAN COLISEO...")
    mapa = Mapa(ancho=6, alto=6)
    mapa.generar_estructura(n_habitaciones=15)
    
    print(f"Coliseo construido: {mapa.ancho}x{mapa.alto} arenas")
    print(f"Arenas disponibles: {len(mapa.habitaciones)}")
    print(f"Arena inicial: [{mapa.habitacion_inicial.x}, {mapa.habitacion_inicial.y}]\n")
    time.sleep(1)
    
    # Colocar contenido en el mapa
    print("UBICANDO DESAFIOS Y RECOMPENSAS...")
    mapa.colocar_contenido(objetos_tesoro, objetos_jefe)
    print("El coliseo esta listo para la batalla!\n")
    time.sleep(1)
    
    # Mostrar estadisticas del mapa
    stats = mapa.obtener_estadisticas_mapa()
    print("ESTADISTICAS DEL COLISEO:")
    print(f"  • Arenas totales: {stats['total_habitaciones']}")
    print(f"  • Conexiones promedio: {stats['promedio_conexiones']}")
    print("  • Distribucion de desafios:")
    for tipo, cantidad in stats['distribucion_contenido'].items():
        if cantidad > 0:
            icono = {"inicial": "[I]", "vacia": "[ ]", "tesoro": "[T]", "monstruo": "[M]", "jefe": "[J]", "evento": "[E]"}.get(tipo, "[·]")
            print(f"    {icono} {tipo}: {cantidad}")
    print()
    time.sleep(2)
    
    # Crear explorador
    explorador = Explorador(mapa)
    
    print("GLADIADOR NOBLE SIX PREPARADO:")
    print(explorador.obtener_estadisticas())
    print(f"Posicion inicial: {explorador.posicion_actual}\n")
    time.sleep(1)
    
    # Mostrar direcciones disponibles
    print("RUTAS INICIALES DISPONIBLES:")
    direcciones = explorador.obtener_habitaciones_adyacentes()
    for dir in direcciones:
        print(f"  => {dir.upper()}")
    print()
    
    # Explorar habitación actual (inicial)
    print("=" * 60)
    print("COMIENZA LA EXPLORACION...")
    print("=" * 60)
    resultado = explorador.explorar_habitacion()
    print(f"{resultado}\n")
    time.sleep(2)
    
    # Mostrar visualizaciones INICIALES
    visualizador = Visualizador()
    
    print("\n" + "VISTA INICIAL DEL COLISEO".center(60, "="))
    visualizador.mostrar_mapa_completo(mapa, explorador)
    visualizador.mostrar_estado_explorador(explorador)
    time.sleep(3)
    

    
    print("\n" + "COMIENZA LA LEYENDA".center(60, "="))
    print("Que los dioses del coliseo te sean favorables!\n")
    
    # Mover y explorar varias habitaciones automáticamente
    movimientos_realizados = 0
    max_movimientos = 8
    
    while movimientos_realizados < max_movimientos and explorador.esta_vivo:
        print(f"\nMOVIMIENTO {movimientos_realizados + 1} DE {max_movimientos}")
        print("-" * 40)
        
        # Obtener direcciones disponibles
        direcciones = explorador.obtener_habitaciones_adyacentes()
        if not direcciones:
            print("CALLEJON SIN SALIDA! La aventura termina aqui...")
            break
            
        # Elegir dirección aleatoria
        direccion = random.choice(direcciones)
        print(f"Navegando al {direccion.upper()}...")
        time.sleep(1)
        
        # Intentar mover
        if explorador.mover(direccion):
            # Explorar la nueva habitación
            print("Explorando la nueva arena...")
            time.sleep(1)
            resultado = explorador.explorar_habitacion()
            print(f"{resultado}")
            
            # Mostrar estado actualizado
            print(f"\n{explorador.obtener_estadisticas()}")
            
            # Mostrar minimapa cada 2 movimientos
            if movimientos_realizados % 2 == 0:
                print("\n" + "VISTA RAPIDA".center(40, "-"))
                visualizador.mostrar_minimapa(mapa, explorador)
        
        movimientos_realizados += 1
        
        # Pausa breve para leer
        if movimientos_realizados < max_movimientos and explorador.esta_vivo:
            input("\nPresiona Enter para continuar tu epopeya...")
    
   
    
    print("\n" + "FIN DE LA EPOPEYA".center(60, "="))
    
    if explorador.esta_vivo:
        print("INCREIBLE! SOBREVIVISTE AL COLISEO DE CAMPEONES!")
    else:
        print("Tu leyenda termina aqui, pero seras recordado...")
    
    print("=" * 60)
    
    # Mostrar resumen final
    visualizador.mostrar_mapa_completo(mapa, explorador)
    visualizador.mostrar_estado_explorador(explorador)
    
    # Estadísticas finales
    habitaciones_exploradas = sum(1 for h in mapa.habitaciones.values() if h.visitada)
    print(f"\nRESUMEN FINAL DE LA GESTA:")
    print(f"  • Arenas exploradas: {habitaciones_exploradas}/{len(mapa.habitaciones)}")
    print(f"  • Reliquias obtenidas: {len(explorador.inventario)}")
    print(f"  • Estado final: {'VICTORIA' if explorador.esta_vivo else 'DERROTA'}")
    
    if explorador.inventario:
        print(f"\nTESOROS LEGENDARIOS OBTENIDOS:")
        for obj in explorador.inventario:
            print(f"  * {obj.nombre} (Valor: {obj.valor} pts)")
    
    # Guardar partida final
    print("\nGUARDANDO TU LEYENDA...")
    Serializador.guardar_partida(mapa, explorador, "leyenda_noble_six.json")
    
    print("\n" + "TU HISTORIA PERDURARA EN LAS CANCIONES".center(60))
    print("La leyenda del Coliseo de Campeones continuara!")

if __name__ == "__main__":
    main()
