from cargaArchivo import CargaArchivo
from validacionAFD import validacionAFD


 
cargador = CargaArchivo()
try:
	ruta = cargador.seleccionarArchivo()
except Exception as error:
	print(error)
try:	
	afd = cargador.cargarArchivo(ruta)
	afd.mostrarDefinicion()
except Exception as error:
	print(error)

try:
	validar = validacionAFD()
	(resultado, errores) = validar.validar_afd(afd)
	print(errores)
	print(resultado)
	afd.mostraTablTransiciones()
except Exception as error:
	print(error)
