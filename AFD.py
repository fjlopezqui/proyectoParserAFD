class AFD:
    def __init__(self, idAFD, estadoInicial):
        self.idAFD = idAFD
        self.estadoInicial = estadoInicial
        self.estadosAFD = set()
        self.estadosAFD.add(estadoInicial)
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

    def agregarEstadoIndv(self, estado):
        if (self.procesar_string(estado)):
            self.estadosAFD.add(estado)
            print("Se agrego el estado '" + estado + "'")

    def agregarEstadoLot(self, listaEstadosComas):
            if (self.procesar_string(listaEstadosComas)):
                listaEstados = listaEstadosComas.split(",")
                for estado in listaEstados:
                    self.estadosAFD.add(estado)
    

    def agregarAlfabeto(self, listaAlfabetoComas):
        if (self.procesar_string(listaAlfabetoComas)):
            listaAlfabeto = listaAlfabetoComas.split(",")
            for simbolo in listaAlfabeto:
                self.alfabetoAFD.add(simbolo)

    def agregarEstadosFinales(self, listaEstadosFinalesComas):
            if (self.procesar_string(listaEstadosFinalesComas)):
                listaEstadosFinales = listaEstadosFinalesComas.split(",")
                for estado in listaEstadosFinales:
                    self.estadosFinales.add(estado)

    def agregarTransicion(self, origen, simbolo, destino):
        validarOrigenVacio = self.procesar_string(origen)
        validarSimboloVacio = self.procesar_string(simbolo)
        validarDestinoVacio = self.procesar_string(destino)
        if (validarDestinoVacio and validarSimboloVacio and validarOrigenVacio):
            if ((simbolo in self.alfabetoAFD) and (origen in self.estadosAFD) and (destino in self.estadosAFD)):
                self.transicionesAFD[(origen, simbolo)] = destino
                print("La transicion fue agregada exitosamente")
            else: 
                print("El simbolo/estado no es valido, chingue a su madre")

    def obtenerTransicion(self, estado, simbolo):
        validarEstadoVacio = self.procesar_string(estado)
        validarSimboloVacio = self.procesar_string(simbolo)
        if (validarSimboloVacio & validarEstadoVacio):
            return self.transicionesAFD.get((estado, simbolo))
                         