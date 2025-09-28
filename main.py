
"""Sebastian Riveros Koenderink - Base de datos 2 - Umag"""

from dungeon_generator.habitacion import Habitacion
from dungeon_generator.objeto import Objeto

def main():
    print("=== Coliseo de campeones ===")
    
    
    Aguijon = Objeto("Aguijon", 100, "De tierras lejanas, se dice que pertenecio a un caballero llamado Hollow Knight")
    print(f"Objeto creado: {Aguijon}")
    
    
    habitacion = Habitacion(1, 0, 0, inicial=True)
    print(f"Habitación creada: {habitacion}")
    
    print("¡Aventurate al coliseo de campeones!")

if __name__ == "__main__":
    main()