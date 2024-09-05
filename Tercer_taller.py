import numpy as np
import os

def ejercicio1():
  os.system('clear')
  array = np.array(range(1,11))
  print('array: ',array)
  
  array_reshaped = array.reshape(2, 5)
  print('Array reshaped (2,5): ',array_reshaped)
  
  print(array_reshaped.shape)
  print(array_reshaped.size)
  print(array_reshaped.ndim)
  input('Presione enter para continuar...')

def ejercicio2():
  os.system('clear')
  a = np.array(range(1,6))
  b = np.array(range(6,11))
  
  print('Array 1: ', a)
  print('Array 2: ', b)
  
  print('a+b: ', a + b)
  print('b-a', b-a)
  print('a*b: ', a*b)
  print('La suma de los elementos de a es: ', np.sum(a))
  input('Presione enter para continuar...')

def ejercicio3():
  os.system('clear')
  
  data = np.array(range(1,11))
  print('data: ', data)
  print('data[4]: ',data[4])
  print('data[2:7]: ', data[2:7])
  
  input('Presione enter para continuar')

def ejercicio4():
  os.system('clear')
  
  array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  print('Array: ', array)
  print('Array+10: ', array+10)
  print('sqrt(Array): ', np.sqrt(array))
  
  input('Presione enter para continuar...')

def ejercicio5():
  os.system('clear')
  
  M = np.array(range(1,7))
  T = np.array([[6,5],[4,3],[2,1]])
  
  M_reshaped = M.reshape(3,2)
  
  print('M: ', M)
  print('M reshaped: ', M_reshaped)
  
  print('M.T: ', M_reshaped.T)
  print('Traspuesta: ', np.dot(M_reshaped, M_reshaped.T))
  
  input('Presione enter para continuar...')

def ejercicio6():
  os.system('clear')

  data = np.array([[2, np.nan, 2], [2, 2, np.nan]]) 

  print ("Input array : ", data) 
    
  out_arr = np.nan_to_num(data, nan=0) 
  print ("output array: ", out_arr) 

  input('Presione enter para continuar')

def ejercicio7():
  os.system('clear')
  
  data = np.array(range(1,1001))
  
  np.save('mi_array.npy', data) # guarda el array data.
  data_loaded = np.load('mi_array.npy') # para cargar el array desde el archivo.
  
  print(data_loaded)
  
  input('Presione enter para continuar')

# Programa principal
def menu():
  os.system('clear')
  print('1. Ejercicio 1')
  print('2. Ejercicio 2')
  print('3. Ejercicio 3')
  print('4. Ejercicio 4')
  print('5. Ejercicio 5')
  print('6. Ejercicio 6')
  print('7. Ejercicio 7')
  print('0. Salir')

def main():
  option = -1
  
  while option != 0:
    menu()
    option = int(input('Ingrese la opción: '))
    if option == 0:
      print('Adios...')
    elif option == 1:
      ejercicio1()
    elif option == 2:
      ejercicio2()
    elif option == 3:
      ejercicio3()
    elif option == 4:
      ejercicio4()
    elif option == 5:
      ejercicio5()
    elif option == 6:
      ejercicio6()
    elif option == 7:
      ejercicio7()
    else:
      print('Opción invalida')
      print('Presione enter para continuar...')

if __name__ == '__main__':
  main()