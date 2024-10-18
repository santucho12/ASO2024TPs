class PolizaInmueble:
    def __init__(self, numero: int, incendio: float, explosion: float, robo: float):
        if not isinstance(numero, int):
            raise ValueError("El número de la póliza debe ser un entero.")
        if not isinstance(incendio, float):
            raise ValueError("El costo del incendio debe ser un número decimal.")
        if not isinstance(explosion, float):
            raise ValueError("El costo de la explosión debe ser un número decimal.")
        if not isinstance(robo, float):
            raise ValueError("El costo del robo debe ser un número decimal.")
        
        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo

    def costoPoliza(self) -> float:
        return self._incendio + self._explosion + self._robo

    def __str__(self) -> str:
        return f"Número de póliza: {self._numero}, Costo incendio: ${self._incendio}, Costo explosión: ${self._explosion}, Costo robo: ${self._robo}"
