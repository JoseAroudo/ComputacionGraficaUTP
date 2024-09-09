import numpy as np

#1) Cree el siguiente vector A= [2, 3,5, 1, 4 ,7 9, 8, 6, 10]

A = np.array([2, 3,5, 1, 4 ,7, 9, 8, 6, 10])
print(A)


#2) Cree un vector B que contenga los elementos desde el 11 hasta el 20 (utilice subscripts)

B = np.arange(11,21)
print(B)


#3) Componer un vector C formado por los vectores A y B en la misma fila respectivamente

C = np.concatenate((A,B))
print(C)


#4) Encuentre el valor mínimo en el vector C haciendo uso de la función propia de Numpy

print("El valor mínimo en el vector C es:",C.min())


#5) Encuentre el valor máximo en el vector C haciendo uso de la función propia de Numpy

print("El valor máximo en el vector C es:",C.max())


#6) Encuentre la longitud en el vector C haciendo uso de la función propia de Numpy

print("La longitud del vector C es:",len(C))



#7) Encentre el promedio de los elementos en el vector C haciendo uso de las operaciones
# elementales suma y división

print("El promedio de los elementos del vector C es:",C.sum()/len(C))


#8) Encuentre el promedio en el vector C haciendo uso de la función propia de Numpy

print("El promedio de los elementos del vector C es:",C.mean())


#9) Encuentre la media en el vector C haciendo uso de la función propia de Numpy

print("La media de los elementos del vector C es:",np.median(C))


#10) Encuentre la suma en el vector C haciendo uso de la función propia de Numpy

print("La suma de los elementos del vector C es:",np.sum(C))


#11) Cree un vector D a partir del vector C con los elementos mayores que 5

D = C[C>5]
print(D)


#12) Cree un vector E a partir del vector C con los elementos mayores que 5 y menores que 15

E= C[(C>5) & (C<15)]
print(E)


#13) Cambie los elementos 5 y 15 elemento del vector C por ‘7’

C[(C==5) | (C==15)] = 7
print(C)

#14) Determine la moda del vector C

moda_result = np.bincount(C).argmax()

print("La moda del vector C es:",moda_result)


#15) Ordene el Vector C de menor a mayor

C.sort()
print(C)


#16) Multiplique el vector C por 10

C = C*10
print(C)


#17) Cambie los elementos del 6 al 8 de la matriz C por 60, 70 y 80 respectivamente

C[5:8] = [60,70,80]


#18) Cambie los elementos del 14 al 16 de la matriz C por 140, 150 y 160 respectivamente

C[13:16] = [140,150,160]
print(C)