class validacionAFD:
    def validar_afd(self, afd):
        errores = []
        resultado = False
        
        # 1. calcular faltantes usando lo que ya armamos
        combinaciones_esperadas = {(estado, simbolo) for estado in afd.estadosAFD for simbolo in afd.alfabetoAFD}
        faltantes = combinaciones_esperadas - set(afd.transicionesAFD.keys())

        # 3. decidir es_valido en base a si errores está vacío o no
        if not faltantes:
            resultado = True
        else:
            for transicion in faltantes:
                errores.append(f"Falta transicion para {transicion}") 
            resultado = False
        
        # 4. retornar algo que le sirva a menu.py para saber TODO: si es válido Y por qué no
        return (resultado, errores)