import os
'''Primer punto
Calculo de caida libre

Escribe un programa en python que calcule y muestre el tiempo que tarda un objeto en caer
desde una altura determinada sin resistencia al aire. utiliza la formula t=((2*h)/g)**(1/2)
donde h es la altura en metros y g es la aceleración debido a la gravedad 9.81 m/s**2'''

def caida_libre(altura):
    g=9.81
    tiempo=((2*altura)/g)**(1/2)
    return tiempo


'''Segundo punto
Conversion de unidades de velocidad
Crea una funcion que convierta la velocidad de km/h a m/s y viceversa.
La funcion debe tomar como argumento el valor de la velocidad y el tipo de conversion'''
def velocidad(velocidad, tipo):
    if tipo == 1:
        valor = velocidad*3.6
        print(f"El valor de la velocidad es: {valor:.2f}km/h")
    elif(tipo== 2):
        valor = velocidad/3.6
        print(f"El valor de la velocidad es: {valor:.2f}m/s")
    else:
        print("No se encontró el tipo de conversion de velocidad, copie y pegue sin espacios lo que aparece")
        tipo = int(input("Digite 1 para hacer converversion km/h a m/s o 2 si es de m/s a km/h\n"))
        velocidad(velocidad, tipo)


'''Tercer punto
Calculo de desplazamiento
Desarrollar un scrip que calcule el desplazamiento de objeto en un movimiento rectilineo uniforme acelerado (MRUA).
Dandonos la velocidad inicial, aceleración y tiempo.
s= ut + (1/2)*a*t**2'''

def MRUA(velinicial, ace, t):
    s= velinicial * t + (1/2)*ace*t**2

    return s

'''Cuarto punto
Suma De Vectores
Implementa una funcion en python que tome 2 vectores representados como una lista y devuelva la suma vectorial'''

def suma_vectores(vector1, vector2, tamano):
    vector3=[]
    for i in range(tamano):
        vector3.append(vector1[i]+vector2[i])

    return vector3

'''Quinto punto
Escribe un Programa que calcule el producto escalar de dos vectores y determine el angulo entre ellos.
Utilizando la formula del coseno del anguló'''

def escalar(vector1, vector2, tamano):
    vector3 = []
    resultado=0
    for i in range(tamano):
        vector3.append(vector1[i] * vector2[i])
    vectorfinal=[abs(i) for i in vector3]

    resultado = sum(vectorfinal)

    return resultado
#todo hacer lo del angulo



'''Sexto punto
Hacer un scrip para calcular el alcance(R) y la altura maxima(H) alcanzada 
por un proyectil lanzado a una velocidad inicial(Vo) a un angulo(teta) con la horizontal.
Ignore la resistencia al aire
'''

def proyectil(velocidad, angulo):
    xmax=0
    ymax=0



def main():
    os.system("cls")
    print("Hola este es el primer taller, se trata de temas basicos de python, más que todo logica")
    print("Se llama:\n FISICA COMPUTACIONAL EN PYTHON\n")
    print("consta de 7 puntos.")
    print("Elige 1 si quieres acceder al punto 'calculo de caida libre'")
    print("Elige 2 si quieres acceder al punto 'conversion de unidades de velocidad'")
    print("Elige 3 si quieres acceder al punto 'Calculo del desplazamiento' ")
    print("Elige 4 si quieres acceder al punto ´suma de vectores'")
    print("Elige 5 si quieres acceder al punto 'producto escalar de vectores'")
    print("Elige 6 si quieres acceder al punto 'lanzamiento de proyectil'")
    print("Elige 7 para volver a la interfaz inicial")

    opcion= int(input("Digite un numero para continuar\n"))

    match opcion:
        case 1:
            os.system("cls")
            alt= float(input("Ingrese la altura en metros del objeto: 2"))
            resultado=caida_libre(alt)
            print(f"El tiempo que tarda el objeto desde una altura de {alt}m es: {resultado:.2f}s")

        case 2:
            os.system("cls")
            vel = float(input("Digite el velocidad del objeto\n"))
            tipo = input("Digite 1 para hacer converversion km/h a m/s o 2 si es de m/s a km/h\n")
            velocidad(vel, tipo)

        case 3:
            os.system("cls")
            vel = float(input("Digite el velocidad inicial del objeto\n"))
            aceleracion= float(input("Digite qué aceleración se le aplicó a este objeto"))
            tiempo=float(input("Digite que está el objeto en el aire\n"))
            MRUA(vel,aceleracion,tiempo)

        case 4:
            os.system("cls")
            vector1= list(input("Ingrese el primer vector\n"))
            vector2= list(input("Ingrese el segundo vector\n"))
            tamano= int(input("Ingrese el tamano de los dos vectores\n"))
            suma_vectores(vector1,vector2,tamano)

        case 5:
            os.system("cls")
            vo= float(input("Digite la velocidad inicial del proyectil\n"))
            angulo= float(input("Digite el angulo que fue lanzado el proyectil inicialmente\n"))
            proyectil(vo, angulo)

        case 6:#todo falta terminar este punto
            os.system("cls")
            print("Primer taller")

        case 7:
            os.system("cls")
            return 0

main()