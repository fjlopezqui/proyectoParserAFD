class AFD:
    def __init__(self):
        self.idAFD = ""
        self.estadoInicial = ""
        self.estadosAFD = set()
        self.alfabetoAFD = set()
        self.estadosFinales = set()
        self.transicionesAFD = {}
        self.esAFDValido = False

    def procesar_string(self, cadena):
        if not isinstance(cadena, str):
            raise TypeError("ERROR: Se esperaba una cadena de texto")

        if not cadena.strip():
            raise ValueError("ERROR: La cadena no puede estar vacia")

        return cadena.strip()

    def agregarIdAFD(self, idAFD):
        idAFDLimpio = self.procesar_string(idAFD)

        if self.idAFD != "":
            raise ValueError(
                f"ERROR: El AFD ya tiene asignado el ID '{self.idAFD}'"
            )

        self.idAFD = idAFDLimpio

    def agregarEstadoInicial(self, estadoInicial):
        estadoInicialLimpio = self.procesar_string(estadoInicial)

        if estadoInicialLimpio not in self.estadosAFD:
            raise ValueError(
                f"ERROR: El estado inicial '{estadoInicialLimpio}' "
                "no pertenece a los estados del AFD"
            )

        self.estadoInicial = estadoInicialLimpio

    def agregarEstadoLot(self, listaEstadosComas):
        listaEstadosComasLimpia = self.procesar_string(listaEstadosComas)

        listaEstados = [
            estado.strip()
            for estado in listaEstadosComasLimpia.split(",")
        ]

        for estado in listaEstados:
            if not estado:
                raise ValueError(
                    "ERROR: No se pueden ingresar estados vacios"
                )

            self.estadosAFD.add(estado)

    def agregarAlfabeto(self, listaAlfabetoComas):
        listaAlfabetoComasLimpia = self.procesar_string(
            listaAlfabetoComas
        )

        listaAlfabeto = [
            simbolo.strip()
            for simbolo in listaAlfabetoComasLimpia.split(",")
        ]

        for simbolo in listaAlfabeto:
            if not simbolo:
                raise ValueError(
                    "ERROR: No se pueden ingresar simbolos vacios"
                )

            self.alfabetoAFD.add(simbolo)

    def agregarEstadosFinales(self, listaEstadosFinalesComas):
        listaEstadosFinalesComasLimpia = self.procesar_string(
            listaEstadosFinalesComas
        )

        listaEstadosFinales = [
            estado.strip()
            for estado in listaEstadosFinalesComasLimpia.split(",")
        ]

        for estado in listaEstadosFinales:
            if not estado:
                raise ValueError(
                    "ERROR: No se pueden ingresar estados finales vacios"
                )

            if estado not in self.estadosAFD:
                raise ValueError(
                    f"ERROR: El estado final '{estado}' "
                    "no pertenece a los estados del AFD"
                )

            self.estadosFinales.add(estado)

    def agregarTransicion(self, origen, simbolo, destino):
        origenLimpio = self.procesar_string(origen)
        simboloLimpio = self.procesar_string(simbolo)
        destinoLimpio = self.procesar_string(destino)

        if origenLimpio not in self.estadosAFD:
            raise ValueError(
                f"ERROR: El estado origen '{origenLimpio}' "
                "no pertenece a los estados"
            )

        if simboloLimpio not in self.alfabetoAFD:
            raise ValueError(
                f"ERROR: El simbolo '{simboloLimpio}' "
                "no pertenece al alfabeto"
            )

        if destinoLimpio not in self.estadosAFD:
            raise ValueError(
                f"ERROR: El estado destino '{destinoLimpio}' "
                "no pertenece a los estados"
            )

        if (origenLimpio, simboloLimpio) in self.transicionesAFD:
            raise ValueError(
                f"ERROR: La transicion para el estado origen "
                f"'{origenLimpio}' y simbolo '{simboloLimpio}' "
                "ya fue registrada"
            )

        self.transicionesAFD[
            (origenLimpio, simboloLimpio)
        ] = destinoLimpio

        print("La transicion fue agregada exitosamente")

    def obtenerTransicion(self, estado, simbolo):
        estadoLimpio = self.procesar_string(estado)
        simboloLimpio = self.procesar_string(simbolo)

        return self.transicionesAFD.get(
            (estadoLimpio, simboloLimpio)
        )

    def marcarValidez(self, esValido):
        if not isinstance(esValido, bool):
            raise TypeError(
                "ERROR: esValido debe ser un valor booleano"
            )

        self.esAFDValido = esValido

    def mostrarDefinicion(self):
        if self.idAFD == "":
            raise ValueError(
                "ERROR: El AFD no tiene un ID asignado"
            )

        print(f"---- QUINTUPLA AFD {self.idAFD} ----")
        print(f"Q (Estados): {self.estadosAFD}")
        print(f"Σ (Alfabeto): {self.alfabetoAFD}")
        print(f"q₀ (Estado inicial): {self.estadoInicial}")
        print(f"F (Estado(s) final(es)): {self.estadosFinales}")
        print("δ (Funciones de transicion):")

        for clave, destino in self.transicionesAFD.items():
            print(f"{clave}: {destino}")

    def mostraTablTransiciones(self):
        estados_ordenados = sorted(self.estadosAFD)
        simbolos_ordenados = sorted(self.alfabetoAFD)

        if not estados_ordenados:
            raise ValueError(
                "ERROR: No existen estados para mostrar"
            )

        if not simbolos_ordenados:
            raise ValueError(
                "ERROR: No existe un alfabeto para mostrar"
            )

        print("\nTABLA DE TRANSICIONES\n")

        print(f"{'Estado':<10}", end="")

        for simbolo in simbolos_ordenados:
            print(f"{simbolo:<10}", end="")

        print()
        print("-" * (10 * (len(simbolos_ordenados) + 1)))

        for estado in estados_ordenados:
            print(f"{estado:<10}", end="")

            for simbolo in simbolos_ordenados:
                siguiente_estado = self.transicionesAFD.get(
                    (estado, simbolo),
                    "-"
                )

                print(f"{siguiente_estado:<10}", end="")

            print()