import numpy as np
import matplotlib.pyplot as plt

#2015.259.22.53.55-C11O_HNE.txt

def obtenerDatos(nombre_archivo):
    datos = np.loadtxt(nombre_archivo)
    return datos
	

def mostrarGraficoAmp(datos_sismograma):
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    print("Generando gr�fico...")
    plt.plot(datos_sismograma)
    print("Gr�fico generado.")
    plt.show()
	
def aplicarTransformada(datos_sismo):
    datos_trans = np.fft.fft(datos_sismo).real
    return datos_trans

def mostrarGraficoFrec(datos_sismograma):
    print("Generando gráfico...")
    plt.plot(datos_sismograma)
    print("Gráfico generado.")
    plt.show()

nombre_archivo = input("Ingrese nombre del archivo (sismograma):\n ")
opcion = input("Mostrar sismograma (amplitud) = 1 |||| Mostrar sismograma (frecuencias) = 2 |||| Mostrar ruido (aprox.) = 3 \n")
datos_sismo = obtenerDatos(nombre_archivo)

if(opcion=='1'):
    mostrarGraficoAmp(datos_sismo)
else:
    if (opcion=='2'):
        datos_transformada = aplicarTransformada(datos_sismo)
        mostrarGraficoFrec(datos_transformada)

    else:
        print("Opci�n inv�lida.")