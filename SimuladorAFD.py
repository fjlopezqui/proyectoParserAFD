class SimuladorAFD:

    # CONSTRUCTOR DE LA CLASE SimuladorAFD
    def __init__(self, automata):
        self.automata = automata


    # ESTA FUNCIÓN SE UTILIZA CUANDO NO HAY NINGÚN
    # AUTÓMATA CARGADO.
    def automata_inexistente(self, cadena):

        return {
            "cadena": cadena,
            "estado_inicial": None,
            "estado_final": None,
            "resultado": "ERROR",
            "aceptada": False,
            "traza": [],
            "mensaje": "El autómata no ha sido definido. Por favor, cargue un autómata antes de evaluar una cadena."
        }


    # FUNCIÓN UTILIZADA PARA EVALUAR UNA CADENA.
    # RECIBE LA CADENA QUE SE QUIERE EVALUAR.
    def evaluar_cadena(self, cadena):

        # Verificar si existe un autómata cargado.
        if self.automata is None:

            return self.automata_inexistente(cadena)


        # Esta lista almacenará la traza de ejecución.
        traza = []


        # El simulador comienza en el estado inicial
        # del autómata.
        estado_actual = self.automata.estadoInicial


        # Guardamos el estado inicial para utilizarlo
        # posteriormente en el resultado.
        estado_inicial = estado_actual


        # VALIDACIÓN DE LA CADENA

        # Recorremos todos los símbolos de la cadena.
        for simbolo in cadena:

            # Verificamos que cada símbolo pertenezca
            # al alfabeto del autómata.
            if simbolo not in self.automata.alfabetoAFD:

                return {
                    "cadena": cadena,
                    "estado_inicial": estado_inicial,
                    "estado_final": estado_actual,
                    "resultado": "ERROR",
                    "aceptada": False,
                    "traza": traza,
                    "mensaje": ("El símbolo '" + simbolo +" no pertenece al alfabeto del autómata.")
                }


        # SIMULACIÓN DEL AUTÓMATA

        # Evaluamos cada símbolo de la cadena.
        # También guardamos el número de paso.
        for numero_de_pasos, simbolo in enumerate(
                cadena, start=1):

            # Guardamos el estado anterior antes
            # de realizar la transición.
            estado_anterior = estado_actual


            # Creamos una clave para buscar la transición.
            transicion = (estado_actual, simbolo)


            # Verificamos si la transición existe.
            if transicion not in self.automata.transicionesAFD:

                # Añadimos este paso a la traza.
                traza.append({
                    "paso": numero_de_pasos,
                    "estado_actual": estado_actual,
                    "simbolo": simbolo,
                    "estado_siguiente": None
                })


                return {
                    "cadena": cadena,
                    "estado_inicial": estado_inicial,
                    "estado_final": estado_actual,
                    "resultado": "ERROR",
                    "aceptada": False,
                    "traza": traza,
                    "mensaje": ("El estado '" + estado_actual + "' no contiene una transición con el símbolo '" + simbolo + "'.")
                }


            # Obtener el estado siguiente utilizando
            # el diccionario de transiciones.
            estado_siguiente = self.automata.transicionesAFD[
                transicion
            ]


            # Añadimos este paso a la traza.
            traza.append({
                "paso": numero_de_pasos,
                "estado_actual": estado_anterior,
                "simbolo": simbolo,
                "estado_siguiente": estado_siguiente
            })


            # Actualizamos el estado actual.
            estado_actual = estado_siguiente


        # VERIFICACIÓN DEL ESTADO FINAL

        # La cadena será aceptada únicamente si el estado
        # final pertenece al conjunto de estados finales.
        aceptada = estado_actual in self.automata.estadosFinales


        # Determinamos el resultado.
        if aceptada == True:

            resultado = "Aceptada"

        else:

            resultado = "Rechazada"


        # Retornamos toda la información de la evaluación.
        return {
            "cadena": cadena,
            "estado_inicial": estado_inicial,
            "estado_final": estado_actual,
            "resultado": resultado,
            "aceptada": aceptada,
            "traza": traza,
            "mensaje": ""
        }


    # FIN DE LA FUNCIÓN evaluar_cadena()


    # ESTA FUNCIÓN SE ENCARGARÁ DE EVALUAR
    # UN LOTE DE CADENAS.
    def evaluar_lote(self, cadenas):

        # Lista donde se almacenarán los resultados.
        resultados = []


        # Evaluamos todas las cadenas de la lista.
        for cadena in cadenas:

            # Utilizamos la función que creamos previamente
            # para evaluar cada cadena individualmente.
            resultado = self.evaluar_cadena(cadena)


            # Agregamos el resultado a la lista.
            resultados.append(resultado)


        return resultados


    # FIN DE LA FUNCIÓN evaluar_lote()


    # ESTA FUNCIÓN SE ENCARGARÁ DE MOSTRAR EN CONSOLA
    # LA TRAZA CREADA PARA UNA CADENA EVALUADA.
    def mostrar_traza(self, resultado):

        # Accedemos a la traza almacenada dentro
        # del resultado de la evaluación.
        traza = resultado["traza"]


        print("TRAZA DE VALIDACIÓN")

        print("Cadena:", resultado["cadena"])

        print("Estado inicial:", resultado["estado_inicial"])

        # Verificar si la cadena no tiene pasos.
        if len(traza) == 0:

            print("\nLa cadena se encuentra vacía...")


        else:

            # Recorrer todos los pasos de la traza.
            for paso in traza:

                print("\nPaso No.", paso["paso"])

                print("Estado actual:", paso["estado_actual"])

                print("Símbolo evaluado:", paso["simbolo"])

                print("Siguiente estado:", paso["estado_siguiente"])


        print("\nEstado final:", resultado["estado_final"])


        # Mostrar el resultado.
        if resultado["resultado"] == "Aceptada":

            print("Resultado: La cadena fue ACEPTADA")


        elif resultado["resultado"] == "Rechazada":

            print("Resultado: La cadena fue RECHAZADA")


        else:

            print("Resultado:", resultado["resultado"])


        # Mostrar mensaje adicional si ocurrió algún error.
        if resultado["mensaje"] != "":

            print("Mensaje:", resultado["mensaje"])