from AFD import AFD
from cargarManual import cargarManual
from cargaArchivo import CargaArchivo
from validacionAFD import validacionAFD
from SimuladorAFD import SimuladorAFD
from Historial import Historial


historial = Historial()
###################################


#Mensaje del menu principal que se imprimira
mensajeMenu = """ /n============= MENU PRINCIPAL =============
    1. Crear un AFD manualmente
    2. Cargar un AFD desde un archivo .txt
    3. Mostrar la definición formal del AFD
    4. Mostrar la tabla de transicion
    5. Validar la estructura del autómata
    6. Evaluar una cadena
    7. Evaluar un archivo de cadenas
    8. Consultar historial de evaluaciones
    9. Cargar o crear otro autómata
    10. Salir
"""

def main():

	afd = AFD()
	crearManual = cargarManual()
	cargarArchivo = CargaArchivo()
	validar = validacionAFD()
	
	while True:
			print(mensajeMenu)
			respuestaUsuario = input("Ingrese una de las opciones: ")
			respuesta = int(respuestaUsuario)

			match (respuesta):
				case 1:
					print("")
					try:
						afd = crearManual.crearAFDManual()
					except Exception as error:
						print(f"Error para cargar AFD manual: {error}")
					
				case 2:
					print("\n==== CARGAR AFD POR ARCHIVO DE TEXTO ====")
					try:
						ruta = cargarArchivo.seleccionarArchivo()
						afd = cargarArchivo.parsearArchivo(ruta)
					except Exception as error:
						print(f"Error para cargar AFD por archivo: {error}")
					
				case 3:
					if (afd):
						afd.mostrarDefinicion()
					else:
						print("Error para mostrar definicion AFD: No se tiene cargado ningun AFD")	
					
				case 4:
					if (afd):
						afd.mostraTablTransiciones()
					else:
						print("Error para mostrar tabla de transiciones AFD: No se tiene cargado ningun AFD")
				case 5:
					try:
						(resultado, errores) = validar.validarAfd(afd)
						afd.esAFDValido = resultado
						if (resultado):
							print(f"RESULTADO: AFD {afd.idAFD} es VÁLIDO")
						else:
							print(f"RESULTADO: AFD {afd.idAFD} es INVÁLIDO")
							print("Lista de errores: ")
							for error in errores:
								print(error)
					except Exception as error:
							print(f"Error para validar AFD: {error}")
				
				case 6:
					if not afd:
						print("Primero debe cargar o crear un AFD.")
					elif not afd.esAFDValido:
						print("No se puede evaluar cadenas de un AFD inválido")
					else:
						cadena = input("Ingrese la cadena que desea evaluar: ")
						
						# Creamos un nuevo simulador, con el AFD actual
						simulador = SimuladorAFD(afd)
	
						# Evaluamos la cadena
						resultado = simulador.evaluar_cadena(cadena)
	
						# Mostramos la traza:
						simulador.mostrar_traza(resultado)
	
						# Lo guardamos en el historial
						historial.agregar_evaluacion(afd, resultado)
	
				case 7:
					if not afd:
						print("Primero debe cargar o crear un AFD.")
					elif not afd.esAFDValido:
						print("No se puede evaluar cadenas de un AFD inválido")
					else:
						ruta = cargarArchivo.seleccionarArchivo()
						try:
							with open(ruta, "r", encoding="utf-8") as archivo:
								cadenas = archivo.readlines()
						except FileNotFoundError:
							raise FileNotFoundError(
								f"No se encontró el archivo en la ruta '{ruta}'."
						)
	
						cadenas = [cadena.strip() for cadena in cadenas]
	
						# Creamos un nuevo simulador, con el AFD actual
						simulador = SimuladorAFD(afd)
	
						# Evaluar todas las cadenas del archivo (Lote):
						resultados = simulador.evaluar_lote(cadenas)
	
						print("\nEVALUACIÓN POR LOTE: ")
	
						for resultado in resultados:
							simulador.mostrar_traza(resultado)
							historial.agregar_evaluacion(afd, resultado)
	
						print("Evaluación por lote finalizada")
				
				case 8:
					historial.mostrar_historial()
					
				case 9:
					print("Reiniciando autómata...")
					afd = None
					
				case 10:
					print("Gracias por usar el programa :)... Cerrando sistema")
					break
	
				case _: 
					print("Opcion invalida: solo se puede obtener una opcion de 1 al 10")

if __name__ == "__main__":

    main()
				
    



 


	
    



 

