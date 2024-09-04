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
    if tipo == 'km/h_to_m/s':
        valor = velocidad/3.6
    elif(tipo== 'm/s_to_km/h'):
        valor = velocidad*3.6
    else:
        print("No se encontró el tipo de conversion de velocidad, copie y pegue sin espacios lo que aparece")
        tipo = input("Digite km/h_to_m/s Ó m/s_to_km/h. Copie y pegue SIN el punto\n")
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
