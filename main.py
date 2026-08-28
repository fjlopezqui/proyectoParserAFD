from AFD import AFD
from cargaArchivo import CargaArchivo

ruta = CargaArchivo.seleccionarArchivo(CargaArchivo);
afd = CargaArchivo.cargarArchivo(CargaArchivo, ruta)
print(afd.idAFD)
print(afd.alfabetoAFD)
print(afd.estadosAFD)
print(afd.estadoInicial)
print(afd.estadosFinales)
print(afd.transicionesAFD)