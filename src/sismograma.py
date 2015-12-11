import numpy as np
import matplotlib.pyplot as plt

#2015.259.22.53.55-C11O_HNE.txt

def obtenerDatos(nombre_archivo):
    datos = np.loadtxt(nombre_archivo)
    return datos
	

def mostrarGraficoAmp(datos_sismograma):
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    print("Generando gráfico...")
    plt.plot(datos_sismograma)
    print("Gráfico generado.")
    plt.show()
	
	
nombre_archivo = input("Ingrese nombre del archivo (sismograma):\n ")
opcion = input("Mostrar sismograma (amplitud) = 1 |||| Mostrar ruido (aprox.) = 2 |||| Mostrar sismograma (frecuencias): \n")
datos_sismo = obtenerDatos(nombre_archivo)
