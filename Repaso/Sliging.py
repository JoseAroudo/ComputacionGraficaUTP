import numpy as np
import matplotlib.pyplot as plt

R=np.array(np.zeros([10,11,3]))

R[0:7,0:1]=[1,1,0]#Amarillo
R[0:7,1:3]=[0,1,1]#AzulClaro
R[0:7,3:5]=[0,1,0]#Verde
R[0:7,5:7]=[1,0,1]#Rosado
R[0:7,7:9]=[1,0,0]#Rojo
R[0:7,9:11]=[0,0,1]#Azul

R[7:10,0:1]=[1]
R[7:10,1:2]=[0.9]
R[7:10,2:3]=[0.8]
R[7:10,3:4]=[0.7]
R[7:10,4:5]=[0.6]
R[7:10,5:6]=[0.5]
R[7:10,6:7]=[0.4]
R[7:10,7:8]=[0.3]
R[7:10,8:9]=[0.2]
R[7:10,9:10]=[0.1]
R[7:10,10:11]=[0]



plt.title("Diagrama de colores")
plt.imshow(R)
plt.show()