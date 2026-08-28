class AFD:
    def __init__(self, idAFD):
        self.idAFD = idAFD
        self.estadoInicial = ""
        self.estadosAFD = set()
        self.alfabetoAFD = set()
        self.estadosFinales = set()
        self.transicionesAFD = {}
        self.esAFDValido = False

    def procesar_string(self, cadena):
        if not isinstance (cadena, str):
            raise TypeError("ERROR: Se esperaba una cadena de texto")
        if not cadena.strip():
            raise ValueError("ERROR: La cadena no puede estar vacia")
        return True

    '''def agregarEstadoIndv(self, estado):
        if (self.procesar_string(estado)):
            self.estadosAFD.add(estado)
            print("Se agrego el estado '" + estado + "'")'''

    def agregarEstadoInicial(self, estadoInicial):
        estadoInicialLimpio = self.procesar_string(estadoInicial)
        if (estadoInicialLimpio):
            if estadoInicial not in self.estadosAFD:
                raise Exception(f"El estado inicial '{estadoInicial}' no pertenece a los estados del AFD")
            self.estadoInicial = estadoInicial;    

    def agregarEstadoLot(self, listaEstadosComas):
            if (self.procesar_string(listaEstadosComas)):
                listaEstados = [estado.strip() for estado in listaEstadosComas.split(",")]
                for estado in listaEstados:
                    self.estadosAFD.add(estado)

    def agregarAlfabeto(self, listaAlfabetoComas):
        if (self.procesar_string(listaAlfabetoComas)):
            listaAlfabeto = [simbolo.strip() for simbolo in listaAlfabetoComas.split(",")]
            for simbolo in listaAlfabeto:
                self.alfabetoAFD.add(simbolo)

    def agregarEstadosFinales(self, listaEstadosFinalesComas):
            if (self.procesar_string(listaEstadosFinalesComas)):
                listaEstadosFinales = [estado.strip() for estado in listaEstadosFinalesComas.split(",")]
                for estado in listaEstadosFinales:
                    if estado not in self.estadosAFD:
                        raise Exception(f"El estado final '{estado}' no pertenece a los estados del AFD")
                    self.estadosFinales.add(estado)

    def agregarTransicion(self, origen, simbolo, destino):
        origenLimpio = self.procesar_string(origen)
        simboloLimpio = self.procesar_string(simbolo)
        destinoLimpio = self.procesar_string(destino)
        if (origenLimpio and simboloLimpio and destinoLimpio):
            if origen not in self.estadosAFD:
                raise Exception(f"El estado origen '{origen}' no pertenece a los estados")
            if simbolo not in self.alfabetoAFD:
                raise Exception(f"El simbolo '{simbolo}' no pertenece al alfabeto")
            if destino not in self.estadosAFD:
                raise Exception(f"El estado destino '{destino}' no pertenece a los estados")
            if (origen, simbolo) in self.transicionesAFD.keys():
                raise Exception(f"La transicion estado origen '{origen}' → simbolo '{simbolo}' ya estaban registrados")
            self.transicionesAFD[(origen, simbolo)] = destino
            print("La transicion fue agregada exitosamente")


    def obtenerTransicion(self, estado, simbolo):
        validarEstadoVacio = self.procesar_string(estado)
        validarSimboloVacio = self.procesar_string(simbolo)
        if (validarSimboloVacio and validarEstadoVacio):
            return self.transicionesAFD.get((estado, simbolo))

    def marcarValidez(self, esValido):
        self.esAFDValido = esValido
                         