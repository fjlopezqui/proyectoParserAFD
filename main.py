from AFD import AFD

afd1 = AFD("automato1", "q0")
afd1.agregarEstadoIndv("q1")
afd1.agregarAlfabeto("0,1")
afd1.agregarEstadosFinales("q1")
afd1.agregarTransicion("q0", "1", "q1")
afd1.agregarTransicion("q1", "0", "q0")
afd1.agregarTransicion("q2", "1", "q1")

print(afd1.estadosAFD)
print(afd1.transicionesAFD)
print(afd1.obtenerTransicion("q1", "0"))
