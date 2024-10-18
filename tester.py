from aseguradora import Aseguradora
from polizaInmueble import PolizaInmueble
from polizaInmuebleEscolar import PolizaInmuebleEscolar

class Tester:
    def run(self):
        aseguradora_1 = Aseguradora()
        aseguradora_2 = Aseguradora()

        poliza_1 = PolizaInmueble(1, 1000.0, 2000.0, 3000.0)
        poliza_2 = PolizaInmueble(2, 1000.0, 2000.0, 3000.0)
        poliza_3 = PolizaInmueble(3, 1000.0, 1500.0, 7000.0)
        poliza_4 = PolizaInmuebleEscolar(4, 1000.0, 1500.0, 7000.0, 80, 2000.0, 3000.0, 4000.0)
        poliza_5 = PolizaInmuebleEscolar(5, 1000.0, 1500.0, 7000.0, 120, 2000.0, 3000.0, 4000.0)

        print(f"Seguros Aseguradora 1: {aseguradora_1.obtenerSeguros()}")
        aseguradora_1.insertar(poliza_2)  # Insertamos póliza número 2
        print(f"Seguros Aseguradora 1: {aseguradora_1.obtenerSeguros()}")  # [2]
        aseguradora_1.insertar(poliza_1)  # Insertamos póliza número 1
        print(f"Seguros Aseguradora 1: {aseguradora_1.obtenerSeguros()}")  # [1, 2] 
        
        print(f"Costo total aseguradora 1: {aseguradora_1.costoTotal()}")  # Costo total de las pólizas en aseguradora 1
        
        aseguradora_2.insertar(poliza_1)
        aseguradora_2.insertar(poliza_2)
        
        print(f"Las 2 aseguradoras tienen las mismas pólizas: {aseguradora_1.esIgual(aseguradora_2)}")  # True
        
        aseguradora_1.insertar(poliza_3)  # Insertamos póliza 3 en aseguradora 1
        
        print(f"Las 2 aseguradoras tienen las mismas pólizas: {aseguradora_1.esIgual(aseguradora_2)}")  # False
        
        aseguradora_1.eliminar(poliza_1)  # Eliminamos póliza 1 de aseguradora 1
        
        print(f"Existe póliza 1 en aseguradora 1: {aseguradora_1.existePoliza(poliza_1)}")  # False
        print(f"Hay pólizas en aseguradora 1: {aseguradora_1.hayPolizas()}")  # True
        print(f"Seguros Aseguradora 1: {aseguradora_1.obtenerSeguros()}")  # [2, 3]

        print(f"Póliza 4: {poliza_4.costoPoliza()}")
        print(f"Póliza 5: {poliza_5.costoPoliza()}")

if __name__ == '__main__':
    Tester().run()
