from polizaInmueble import PolizaInmueble

class Aseguradora:
    def __init__(self, seguros=None):
        if seguros is None:
            self._seguros = []
        elif not all(isinstance(seguro, PolizaInmueble) for seguro in seguros):
            raise ValueError("Todos los argumentos deben ser instancias de PolizaInmueble")
        else:
            self._seguros = seguros

    def obtenerSeguros(self):
        return self._seguros  

    def insertar(self, poliza: PolizaInmueble):
        if not isinstance(poliza, PolizaInmueble):
            raise ValueError("El argumento debe ser una instancia de PolizaInmueble")
        self._seguros.append(poliza)

    def eliminar(self, poliza: PolizaInmueble):
        self._seguros.remove(poliza)

    def existePoliza(self, poliza: PolizaInmueble) -> bool:
        return poliza in self._seguros

    def hayPolizas(self) -> bool:
        return bool(self._seguros)

    def costoTotal(self) -> float:
        return sum(seguro.costoPoliza() for seguro in self._seguros)

    def esIgual(self, aseguradora: 'Aseguradora') -> bool:
        return self.obtenerSeguros() == aseguradora.obtenerSeguros()
