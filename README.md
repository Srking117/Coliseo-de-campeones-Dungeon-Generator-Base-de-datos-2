# Generador de Mapas de Dungeon - Coliseo de Campeones

Tarea 1 - Bases de Datos II
Sebastian Riveros Koenderink
Umag

## Instrucciones de instalacion

1. Crear entorno virtual: `python -m venv venv`
2. Activar entorno: `.\venv\Scripts\activate`  // o `source venv/bin/activate` (Linux/Mac)
3. Instalar dependencias: `pip install rich`
4. Ejecutar: `python main.py`

## Comentarios:

Bievenido al coliseo de campeones, principalmente escogi esta tematica como referencia a varios videojuegos
haciendo referencia a los siguientes: Red dead redemption, Hollow Knight, Thanos, Megatron, Teemo, Revolver Ocelot ("Metal Gear Solid), Kratos de god of war y asi entre muchos como gengar de pokemon y el personaje principal el Noble Six en referencia a halo reach...


⠀⠀⠀⠀⠀ ⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⡴⠞⠉⢉⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢯⡉⠙⠳⣦⡀⠀⠀                
⢀⣼⠋⠀⠀⢀⣤⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠈⠻⣆⠀
⣼⠃⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠹⡇
⡟⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀ ⠀⣿
⣿⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⢠⡿
⠘⣷⡀⠀⠘⢷⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣴⠟⠁⠀⣠⡾⠁
⠀⠈⠻⣦⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⣼⠋⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⢸⡇⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⢸⡇⠀⠀
⠀⠀⠀⢸⡇⢠⣶⣿⣿⣦⡀⠀⠀⠀  ⡠⣦⣿⣷⣦⡀⢸⡇⠀⠀⠀
⠀⠀⠀⠸⡇⣿⣿⣿⣿⣿⣶⠀⠀⠀  ⣿⣿⣿⣿⣿⣶⢸⡇⠀⠀⠀
⠀⠀⠀⢰⣇⢻⣿⣿⣿⣿⡟⠀⠀⠀  ⢿⣿⣿⣿⣟⡟⣼⠃⠀⠀⠀
⠀⠀⠀⠀⣻⣆⠙⠛⠛⠋⠀⠀⠀⠀  ⠈⠙ ⠛⠛⢁⣴⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠻⣿⡿⣶⣦⣤⣤⣀⣀⣀⣀⣤⣤⡶⠖⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢻⡆⣱⣾⠟⠉⣽⢋⡟⣯⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣿⠟⠁⣠⡾⠁⠜⢸⡉⠁⡽⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡏⣠⡾⠋⢀⠆⠀⣼⢷⡀⠸⣽⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⡿⠉⣀⡴⠋⠀⣰⢿⠀⠻⣄⢹⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣡⡾⠋⠀⣠⣷⣿⡈⢧⡀⠘⣾⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠏⠄⢠⣾⣿⣿⣿⣿⣌⠳⣄⢹⡷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣧⡷⠏⣿⣿⡏⠈⣿⣿⣿⣾⣿⠛⠻⠷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠀ ⠀⢹⣿⡇ ⠀⣿⡟⠈⠉⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠉⠀     ⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀




## Cumplimiento de Requerimientos

Requerimiento	Estado	         Detalles
1. Clase Habitacion	           Cumplido	Atributos: id, coordenadas, inicial, contenido, conexiones, visitada
2. Clase Mapa	                 Cumplido	Generación procedural, contenido, validaciones de tamaño
3. Clase Objeto	               Cumplido	nombre, valor, descripción, serialización
4. Clase Explorador	           Cumplido	vida, inventario, movimiento, combate, interacción
5. ContenidoHabitacion	       Cumplido	Tesoro, Monstruo, Jefe con métodos abstractos
6. Distribución contenido	     Cumplido	20-30% monstruos, 15-25% tesoros, 5-10% eventos, 1 jefe
7. Estadísticas mapa	         Cumplido	Total habitaciones, distribución, promedio conexiones
8. Serialización JSON	         Cumplido	Guardar/cargar partidas completas
9. Visualizador Rich	         Cumplido	4 visualizaciones: mapa completo, habitación actual, minimapa, estado
10. Sistema eventos	           Cumplido	5 tipos de eventos integrados en distribución
11. Dificultad escalable	     Cumplido	Basada en distancia Manhattan, documentada



