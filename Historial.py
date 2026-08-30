class Historial:

    # CONSTRUCTOR DE LA CLASE HISTORIAL
    def __init__(self):
        self.evaluaciones = []

    # ESTA FUNCIÓN AGREGA UNA NUEVA EVALUACIÓN A LA LISTA DE EVALUACIONES, REQUIERE EL RESULTADO OBTENIDO
    # DEL SIMULADOR, ADEMÁS DEL NOMBRE DEL AUTÓMATA CON EL QUE SE REALIZÓ LA SIMULACIÓN.
    def agregar_evaluacion(self, afd, resultado):
 
        # Crear una copia de la información del resultado.
        evaluacion = {
            "automata": afd,
        
            "cadena": resultado["cadena"],
            "estado_inicial": resultado["estado_inicial"],
            "estado_final": resultado["estado_final"],
            "resultado": resultado["resultado"],
            "aceptada": resultado["aceptada"],
            "traza": resultado["traza"],
            "mensaje": resultado["mensaje"]
        }

        # Agregar la evaluación a la lista.
        self.evaluaciones.append(evaluacion)

    # FUNCIÓN QUE DEVUELVE LAS EVALUACIONES REALIZADAS!
    def obtener_evaluaciones(self):
        return self.evaluaciones

    # ESTA FUNCIÓN MUESTRA EL HISTORIAL COMPLETO:
    def mostrar_historial(self):

        # Primero verifica si, efectivamente, hay algo en historial :p
        if len(self.evaluaciones) == 0:

            print("El historial se encuentra vacío")
            return

        print("HISTORIAL DE EVALUACIONES: ")

        # Recorremos todas las evaluaciones almacenadas en la lista de evaluaciones
        for numero, evaluacion in enumerate(self.evaluaciones, start=1):

            print("")
            print("Evaluación", numero)
            print("----------------------------------------")
            print("")

            print("Autómata:")
            evaluacion["automata"].mostrarDefinicion()

            print("Cadena:", evaluacion["cadena"])

            print("Estado inicial:", evaluacion["estado_inicial"])

            print("Estado final:", evaluacion["estado_final"])

            print("Resultado:", evaluacion["resultado"])

            # Mostrar si fue aceptada o rechazada.
            if evaluacion["aceptada"]:

                print("La cadena fue: ACEPTADA")

            else:

                print("La cadena fue: RECHAZADA")

            # Aquí mostramos si apareció algún mensaje de error.
            if evaluacion["mensaje"] != "":

                print("Mensaje:", evaluacion["mensaje"])

        print("")
        print("----------------------------------")

    
    # FUNCIÓN POR SI SE QUIERE LIMPIAR EL HISTORIAL (Creo que no la vamos a usar, pero igual es bueno tenerla >:)   )
    def limpiar(self):

        self.evaluaciones.clear()

        print("")
        print("El historial ha sido limpiado.")