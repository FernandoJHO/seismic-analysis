import numpy as np
import scipy.fftpack as sci
import matplotlib.pyplot as plt


# 2015.259.22.53.55-C11O_HNE.txt

def obtenerDatos(nombre_archivo):
    datos = np.loadtxt(nombre_archivo)
    return datos


def obtenerRuido(datos):
    datos_ruido = []
    for i in range(0, 101):
        datos_ruido.append(datos[i])
    return datos_ruido


def espectroFrecuencia(datos_sismo):
    #datos_trans = np.fft.fft(datos_sismo).real
    datos_trans = np.fft.fft(datos_sismo)
    datos_trans_freq = np.fft.fftfreq(len(datos_trans),0.5)
    plt.plot(datos_trans_freq, np.abs(datos_trans))
    plt.grid()
    plt.show()
    #return datos_trans


def mostrarGrafico(datos_sismograma):
    print("Generando gráfico...")
    plt.plot(datos_sismograma)
    print("Gráfico generado.")
    plt.show()


def classicSTALTAPy(a, nsta=5 * 200, nlta=10 * 200):
    sta = np.cumsum(a ** 2)

    sta = np.require(sta, dtype=np.float)

    lta = sta.copy()

    sta[nsta:] = sta[nsta:] - sta[:-nsta]
    sta /= nsta
    lta[nlta:] = lta[nlta:] - lta[:-nlta]
    lta /= nlta

    sta[:nlta - 1] = 0

    dtiny = np.finfo(0.0).tiny
    idx = lta < dtiny
    lta[idx] = dtiny

    return sta / lta


nombre_archivo = input("Ingrese nombre del archivo (sismograma):\n ")
opcion = input(
    "Mostrar sismograma (amplitud) = 1 |||| Mostrar ruido (aprox.) = 2 |||| Mostrar sismograma (frecuencias) = 3 |||| Mostrar gráfico STA/LTA = 4: \n")
datos_sismo = obtenerDatos(nombre_archivo)

if opcion == '1':
    mostrarGrafico(datos_sismo)
else:
    if opcion == '2':
        datos_ruido = obtenerRuido(datos_sismo)
        mostrarGrafico(datos_ruido)
    else:
        if opcion == '3':
            #espectro_frecuencia =
            espectroFrecuencia(datos_sismo)
            #mostrarGrafico(espectro_frecuencia)
        else:
            if opcion == '4':
                sta_lta = classicSTALTAPy(datos_sismo)
                mostrarGrafico(sta_lta)
            else:
                print("Opción inválida.")
