import interfaces.interfazTaller1
import interfazTaller1, interfazTaller2, interfazTaller3, interfazTaller4, interfazTaller5, interfazTaller6, interfazTaller7
import os
def main():
    print("#"*70)
    print("#"*30,"Interfaz","#"*30)
    print("#" * 70)
    print("Presione 1 para elegir el primer taller")
    print("Presione 2 para elegir el segundo taller")
    print("Presione 3 para elegir el tercero taller")
    print("Presione 4 para elegir el cuarto taller")
    print("Presione 5 para elegir el quinto taller")
    print("Presione 6 para elegir el sexto taller")
    print("Presione 7 para salirse del taller")
    opcion=input("Escoja el opcion: \n")

    match opcion:
        case "1":
            os.system('cls')
            interfazTaller1.main()


main()