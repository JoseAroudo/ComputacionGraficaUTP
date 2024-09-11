import numpy as np
import matplotlib.pyplot as plt
import math


def MiSeno(x):
    s=0
    n=0
    AporteMin=0.00001
    while(True):
        Termino=((-1)**n/(math.factorial(2*n+1)))*(x**(2*n+1))
        s+=Termino
        n+=1
        if (math.fabs(Termino) < AporteMin):
            break
    return s


def MiCoseno(x):
    s=0
    n=0
    AporteMin=0.0000001
    while(True):
        Termino=((-1)**n/(math.factorial(2*n)))*(x**(2*n))
        s+=Termino
        n+=1
        if (math.fabs(Termino) < AporteMin):
            return s



def MiTangente(x):
    s=0
    Termino=MiSeno(x)/MiCoseno(x)
    s+=Termino
    return s



def MiExponencial(x):
    s=0
    n=0
    AporteMin=0.0000001
    while(True):
        Termino=(x**n)/math.factorial(n)
        s+=Termino
        n+=1
        if (math.fabs(Termino) < AporteMin):
            return s


def MiLogaritmo(x):
    s=0
    n=1
    AporteMin=1e-8
    while(True):
        Termino=((-1)**(n+1))*((x**n)/n)
        s+=Termino
        n+=1
        if (math.fabs(Termino) < AporteMin):
            return s


"""
Definicion de las funciones ufunc para poder trabajar con arreglos y
la funcion la tome como 1 sola entrada.
"""
MiSeno= np.frompyfunc(MiSeno,1,1)
MiCoseno= np.frompyfunc(MiCoseno,1,1)
MiTangente= np.frompyfunc(MiTangente,1,1)
MiExponencial= np.frompyfunc(MiExponencial,1,1)
MiLogaritmo= np.frompyfunc(MiLogaritmo,1,1)


def Graficas():
    plt.figure("Series de Taylor")
    e=np.linspace(0,2*np.pi,50)

    plt.subplot(3,3,1)
    d=MiSeno(e)
    plt.plot(e,d)
    plt.grid()
    plt.title("Funcion Seno")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")

    plt.subplot(3,3,2)
    f=MiCoseno(e)
    plt.plot(e,f)
    plt.grid()
    plt.title("Funcion Coseno")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")

    plt.subplot(3,3,3)
    g=MiTangente(e)
    plt.plot(e,g)
    plt.grid()
    plt.title("Funcion Tangente")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")

    plt.subplot(3,3,7)
    h=MiExponencial(e)
    plt.plot(e,h)
    plt.grid()
    plt.title("Funcion Exponencial")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")

    plt.subplot(3,3,8)
    e=np.linspace(-0.9,0.9,50) #Se define otro rango para que la grafica de logaritmo sea evidente.
    i=MiLogaritmo(e)
    plt.plot(e,i)
    plt.grid()
    plt.title("Funcion Logaritmo")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.show()


Graficas()