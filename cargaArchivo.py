import re
import tkinter as tk
from tkinter import filedialog
from AFD import AFD


class CargaArchivo:
    """
    Clase encargada de leer y parsear el archivo .txt que define un AFD,
    según el formato:

        NOMBRE=AFD_AB
        ESTADOS=q0,q1,q2
        ALFABETO=a,b
        INICIAL=q0
        FINALES=q2
        TRANSICIONES:
        q0,a,q1
        q0,b,q0
        ...

    Responsabilidades:
    - cargarArchivo(): método PÚBLICO. Punto de entrada. Abre el archivo,
      delega el parsing a parsearArchivo() y devuelve el AFD construido.
    - parsearArchivo(): método interno. Recibe la lista de líneas ya leída
      e interpreta su contenido, construyendo el AFD paso a paso.

    Principio de errores: cada línea se procesa dentro de un try/except que
    NO atrapa el error de forma final, sino que lo vuelve a lanzar (raise)
    enriquecido con el número de línea. Así el procesamiento se detiene en
    el primer error (según lo acordado), y es quien LLAMA a cargarArchivo()
    (por ejemplo menu.py) quien decide cómo mostrarlo al usuario.
    """

    PATRON_TRANSICION = r"^\w+,\w+,\w+$"
    PATRON_CLAVE_VALOR = r"^\w+=\w+(,\w+)*$"

    def seleccionarArchivo(self):
        """
        Abre el explorador de archivos del sistema operativo para que el
        usuario elija el .txt del AFD, en vez de tener que escribir la ruta
        a mano. Devuelve la ruta elegida como string, o "" si el usuario
        cierra el diálogo sin elegir nada.
        """
        ventanaRaiz = tk.Tk()
        ventanaRaiz.withdraw()  # oculta la ventana vacía de tkinter, solo queremos el diálogo

        rutaArchivo = filedialog.askopenfilename(
            title="Seleccione el archivo del AFD",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )

        ventanaRaiz.destroy()
        return rutaArchivo

    def cargarArchivo(self, rutaArchivo):
        """
        Método público: abre el archivo, maneja el caso de archivo
        inexistente, y delega la interpretación del contenido a
        parsearArchivo(). Devuelve el objeto AFD ya construido.
        """
        try:
            with open(rutaArchivo, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"No se encontró el archivo en la ruta '{rutaArchivo}'."
            )

        return self.parsearArchivo(lineas)

    def parsearArchivo(self, lineas):
        """
        Recibe una lista de líneas (ya leídas, sin depender del disco) e
        interpreta cada una según en qué "zona" del archivo se encuentre:

        - Zona 1 (antes de 'TRANSICIONES:'): líneas CLAVE=valor. Se van
          guardando en un diccionario intermedio.
        - Zona 2 (después de 'TRANSICIONES:'): líneas origen,simbolo,destino.
          Se validan con regex y se guardan en una lista temporal, porque
          todavía no existe el objeto AFD (falta ESTADOS y ALFABETO para
          poder llamar a agregarTransicion sin que falle).

        Al final, con la zona 1 completa, se construye el AFD y recién ahí
        se cargan las transiciones acumuladas.
        """
        datosClaveValor = {}
        transicionesPendientes = []
        modoTransiciones = False

        for numeroLinea, lineaCruda in enumerate(lineas, start=1):
            linea = lineaCruda.strip()

            if not linea:
                continue  # ignorar líneas vacías

            try:
                if linea.upper() == "TRANSICIONES:":
                    modoTransiciones = True
                    continue

                if not modoTransiciones:
                    # Zona 1: CLAVE=valor (validada con regex antes de extraer)
                    if not re.match(self.PATRON_CLAVE_VALOR, linea):
                        raise ValueError(
                            f"la línea '{linea}' no cumple el formato 'CLAVE=valor'"
                        )
                    clave, valor = linea.split("=", 1)
                    clave = clave.strip().upper()
                    valor = valor.strip()
                    datosClaveValor[clave] = valor

                else:
                    # Zona 2: origen,simbolo,destino
                    if not re.match(self.PATRON_TRANSICION, linea):
                        raise ValueError(
                            f"la transición '{linea}' no cumple el formato 'origen,simbolo,destino'"
                        )
                    origen, simbolo, destino = linea.split(",")
                    transicionesPendientes.append((origen, simbolo, destino))

            except Exception as error:
                raise Exception(f"Error en línea {numeroLinea}: {error}")

        return self._construirAFD(datosClaveValor, transicionesPendientes)

    def _construirAFD(self, datos, transiciones):
        """
        Construye el objeto AFD a partir del diccionario de la zona 1 y la
        lista de transiciones de la zona 2. Reutiliza los métodos de AFD
        (que ya validan y lanzan), en el orden correcto: primero estados y
        alfabeto, luego inicial/finales, y al final las transiciones.
        """
        for claveRequerida in ("NOMBRE", "ESTADOS", "ALFABETO", "INICIAL", "FINALES"):
            if claveRequerida not in datos:
                raise Exception(f"Falta la clave obligatoria '{claveRequerida}' en el archivo")

        try:
            afd = AFD
            afd.agregarIdAFD(datos["NOMBRE"])
            afd.agregarEstadoLot(datos["ESTADOS"])
            afd.agregarAlfabeto(datos["ALFABETO"])
            afd.agregarEstadoInicial(datos["INICIAL"])
            afd.agregarEstadosFinales(datos["FINALES"])

            for origen, simbolo, destino in transiciones:
                afd.agregarTransicion(origen, simbolo, destino)
            return afd
        except Exception as error:
            raise Exception(f"Error de carga del archivo: {error}")

        