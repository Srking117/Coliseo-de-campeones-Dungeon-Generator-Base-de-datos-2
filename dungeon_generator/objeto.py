class Objeto:
    """ elementos obtenibles en el mapa"""
    
    def __init__(self, nombre: str, valor: int, descripcion: str):
        self.nombre = nombre
        self.valor = valor
        self.descripcion = descripcion
    
    def __str__(self) -> str:
        return f"{self.nombre} (Valor: {self.valor}) - {self.descripcion}"
    
    def to_dict(self) -> dict:
        """Convierte el objeto a diccionario para serialización"""
        return {
            "nombre": self.nombre,
            "valor": self.valor,
            "descripcion": self.descripcion
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Objeto':
        """Crea un objeto desde un diccionario"""
        return cls(
            nombre=data["nombre"],
            valor=data["valor"],
            descripcion=data["descripcion"]
        )