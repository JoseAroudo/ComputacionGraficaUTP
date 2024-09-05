import Primer_Taller, interfaz_MAIN
import os

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
            alt= float(input("Ingrese la altura del punto "))
            resultado=Primer_Taller.caida_libre(alt)
            print(f"El tiempo que tarda el objeto desde una altura de {alt}m es: {resultado:.2f}s")

        case 2:
            os.system("cls")
            vel = float(input("Digite el velocidad del punto\n"))
            tipo = input("Digite km/h_to_m/s Ó m/s_to_km/h\n")
            Primer_Taller.velocidad(vel,tipo)

        case 3:
            os.system("cls")
            vel = float(input("Digite el velocidad inicial del objeto\n"))
            aceleracion= float(input("Digite qué aceleración se le aplicó a este objeto"))
            tiempo=float(input("Digite que está el objeto en el aire\n"))
            Primer_Taller.MRUA(vel,aceleracion,tiempo)

        case 4:
            os.system("cls")
            vector1= list(input("Ingrese el primer vector\n"))
            vector2= list(input("Ingrese el segundo vector\n"))
            tamano= int(input("Ingrese el tamano de los dos vectores\n"))
            Primer_Taller.suma_vectores(vector1,vector2,tamano)

        case 5:
            os.system("cls")
            vo= float(input("Digite la velocidad inicial del proyectil\n"))
            angulo= float(input("Digite el angulo que fue lanzado el proyectil inicialmente\n"))
            Primer_Taller.proyectil(vo, angulo)

        case 6:#todo falta terminar este punto
            os.system("cls")
            print("Primer taller")

        case 7:
            os.system("cls")
            interfaz_MAIN.main()