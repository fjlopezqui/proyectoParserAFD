from AFD import AFD

class cargarManual:    
    def __init__(self, idAFD):
        self.AFD = AFD(idAFD)

    def agregarEstadosAFD(self):
        listaEstados = input(f"Ingrese la lista de estados para el AFD '{self.AFD.idAFD}' (debe estar separada en comas): ")
        try:
            self.AFD.agregarEstadoLot(listaEstados)
            print("Se ingresaron los estados correctamente")
            return True
        except Exception as error:
            print(error)
            return False

    def agregarTransicionesAFD(self):
        while (respuestaUsuario := input(f"¿Deseas agregar transicion al AFD {self.AFD.idAFD}? (y/n): ").strip().lower()) != "n":
            print("Transiciones actuales")
            if not self.AFD.transicionesAFD:
                print("     (No hay transiciones registradas)")
            else:
                for (origen, simbolo), destino in self.AFD.transicionesAFD.items():
                    print(f"    ({origen}, '{simbolo}') -> {destino}")
            print("Usando como base el formato δ(q, a) = p")
            #1. pedir origen
            origen = input("Ingrese el estado de origen (q) de la transicion: ")
            #2. pedir simbolo
            simbolo = input("Ingrese el simbolo (a) de la transicion: ")
            #3. pedir destino
            destino = input("Ingrese el estado de destino (p) de la transicion:")

            try:
                self.AFD.agregarTransicion(origen, simbolo, destino)
            except Exception as error:
                print(error)
    
    def agregarEstadoInicial(self):
        estadoInicial = input(f"Ingrese el estado inicial del AFD '{self.AFD.idAFD}': ")
        try:
            self.AFD.agregarEstadoInicial(estadoInicial)
            return True
        except Exception as error:
            print(error)
            return False

    def agregarEstadosFinales(self):
        listaEstadosFinales = input(f"Ingrese la lista de estados finalaes para el AFD '{self.AFD.idAFD}' (debe estar separada en comas): ")
        try:
            self.AFD.agregarEstadosFinales(listaEstadosFinales)
            print("Se ingresaron los estados correctamente")
            return True
        except Exception as error:
            print(error) 
            return False

    def agregarAlfabeto(self):
        alfabeto = input(f"Ingrese la lista de los simbolos del alfabeto permitido en el AFD '{self.AFD.idAFD}' (debe estar separada en comas): ")
        try:
            self.AFD.agregarAlfabeto(alfabeto)
            print("Se ingresaron los estados correctamente")
            return True
        except Exception as error:
            print(error)         
            return False 


    def crearAFDManual(self):
        idAFD = self.AFD.idAFD
        print(f"==== CREAR AFD {idAFD} ====")
        print("1. AGREGAR ALFABETO DEL AUTOMATA FINITO")
        while True:
            validarSalida = self.agregarAlfabeto()
            if validarSalida: break 
        print("2. AGREGAR ESTADOS DEL AUTOMATA FINITO")
        while True:
            validarSalida = self.agregarEstadosAFD()
            if validarSalida: break
        print("3. AGREGAR ESTADO INCIAL DEL AUTOMATA FINITO")
        while True:
            validarSalida = self.agregarEstadoInicial()
            if validarSalida: break
        print("4. AGREGAR ESTADO FINAL DEL AUTOMATA FINITO")
        while True:
            validarSalida = self.agregarEstadosFinales()
            if validarSalida: break
        print("5. AGREGAR FUNCIONES DE TRANSICION DEL AUTOMATA FINITO")
        self.agregarTransicionesAFD()
        return self.AFD

