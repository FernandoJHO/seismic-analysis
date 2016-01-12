import numpy as np
import scipy as sci
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
    largo = len(datos_sismo)
    datos_frq = sci.fft(datos_sismo) / largo
    datos_frq = datos_frq[range(round(largo / 2))]

    return datos_frq

def mostrarGraficoFrecuencia(datos_sismo):

    tasa = 0.5
    largo = len(datos_sismo)
    k = sci.arange(largo)
    t = largo / tasa
    freq = k / t
    freq = freq[range(round(largo / 2))]

    datos_frq = sci.fft(datos_sismo) / largo
    datos_frq = datos_frq[range(round(largo / 2))]

    plt.plot(freq, abs(datos_frq))
    plt.show()

def mostrarGraficoTiempo(datos_sismograma):
    tasa = 0.5
    t = np.linspace(0, (len(datos_sismograma / tasa)), len(datos_sismograma))
    plt.plot(t, datos_sismograma)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.show()

def low_pass_filter(x, samples = 20):
    a = np.fft.rfft(x)
    tot = len(a)
    for x in range(tot-samples):
        a[samples + x] = 0.0
    #plt.plot(np.fft.irfft(a))
    #plt.show()
    return np.fft.irfft(a)

def classicSTALTAPy(a, nsta= 0.5*100, nlta= 0.5*200):
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

def graf(datos):
    plt.plot(datos)
    plt.show()

nombre_archivo = input("Ingrese nombre del archivo (sismograma):\n ")
opcion = input(
    "Mostrar sismograma (amplitud) = 1 |||| Mostrar ruido (aprox.) = 2 |||| Mostrar sismograma (frecuencias) = 3 |||| Mostrar gráfico STA/LTA = 4: \n")
datos_sismo = obtenerDatos(nombre_archivo)

if opcion == '1':
    mostrarGraficoTiempo(datos_sismo)
else:
    if opcion == '2':
        datos_ruido = obtenerRuido(datos_sismo)
        mostrarGraficoTiempo(datos_ruido)
    else:
        if opcion == '3':
            mostrarGraficoFrecuencia(datos_sismo)
        else:
            if opcion == '4':
                datos_freq = espectroFrecuencia(datos_sismo)
                datos_filtrados = low_pass_filter(datos_freq)
                sta_lta = classicSTALTAPy(datos_filtrados)
                graf(sta_lta)
                #mostrarGraficoTiempo(sta_lta)
            else:
                print("Opción inválida.")
