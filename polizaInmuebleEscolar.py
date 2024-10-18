from polizaInmueble import PolizaInmueble

class PolizaInmuebleEscolar(PolizaInmueble):
    def __init__(self, cantPersonas: int, montoEquipamento: float, montoMobiliario: float, montoPersona: float, numero: int, incendio: float, explosion: float, robo: float):
        super().__init__(numero, incendio, explosion, robo)
        if not isinstance(cantPersonas, int):
            raise ValueError("cantPersonas debe ser un número entero")
        if not isinstance(montoEquipamento, float):
            raise ValueError("montoEquipamento debe ser un número")
        if not isinstance(montoMobiliario, float):
            raise ValueError("montoMobiliario debe ser un número")
        if not isinstance(montoPersona, float):
            raise ValueError("montoPersona debe ser un número")

        self._cantPersonas = cantPersonas
        self._montoEquipamento = montoEquipamento
        self._montoMobiliario = montoMobiliario
        self._montoPersona = montoPersona

    def costoPoliza(self) -> float:
        return super().costoPoliza() + self._cantPersonas * self._montoPersona + self._montoEquipamento + self._montoMobiliario 
