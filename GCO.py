#  PDF describiendo el analisis realizado en varios ejemplos y las conclusiones extraidas.
import numpy as np
from numpy import mean
import pandas as pd
import argparse
from numpy.linalg import norm

# para ejecutar de momento (solo leyendo el fichero de entrada): python3 GCO.py -fichL pruebaGCO.txt 
from numpy.core.fromnumeric import transpose

#Lee por linea de comandos e imprime
parser = argparse.ArgumentParser(description='Sistema recomedador')
parser.add_argument('-fichL', '--fichero_lectura', type = str, help='Nombre fichero lectura')
args = parser.parse_args()
variables = vars(args)
#print(variables)

indices_incognitas = []

def lectura_fichero(nombre_fichero):

    A = np.loadtxt(nombre_fichero, dtype='S') #'S' trata el dato como numero
    print("MATRIZ ORIGINAL")
    print(A)
    # 1 localizar las incognitas
    global indices_incognitas # indica que quiero modificar la variable global
    indices_incognitas = np.where(A == '-')
    # indices_incognitas = index
    print("INDICES:")
    print(indices_incognitas)
    # print(index)
              
    # 2 eliminamos las columnas que contengan las incognitas
    A1 = np.delete(A, indices_incognitas[1], axis=1) #axis = 1 indica que haga la operacion por columnas
    # 3 pasar la matriz a entero
    print("MATRIZ CON COLUMNAS ELIMINADAS:")
    # print(A1)
    A2 = A1.astype(int) #convierte la matriz string a matriz int
    print(A2)

    return A2




def correlacion_pearson(matriz):
    # convertimos la matriz a dataframe 
    # data_frame = pd.DataFrame(matriz)
    # print(data_frame)
    # corr_data = data_frame.corr()
    # print(corr_data)
    # media2 = data_frame[0].corr(data_frame[1], method='pearson')
    # print(media2)
    
    # IDEA: creamos un bucle con los indices de las incognitas y, dentro del bucle,
    #       creamos otro que hace la correlacion_pearson de la posicion de la incognita
    #       con las filas de la matriz. Como la correlacion que hace numpy da una matriz 2x2,
    #       y nosotros escogemos una celda, ese valor lo guardamos en una lista. Para que asi,
    #       la matriz de la correlacion tenga cada fila la lista de la correlacion de cada incognita
    
    # calculamos la media de cada fila (fila equivale a persona)
    media = np.mean(matriz, axis=1)
    print(media)
    corr_data = np.corrcoef(matriz[indices_incognitas[0]], matriz[1])[1,0]
    print(corr_data)
    
    dist_euclide = np.linalg.norm(matriz[indices_incognitas[0]] - matriz[1])
    print(dist_euclide)
    
    result_coseno = np.dot(matriz[indices_incognitas[0]], matriz[1])/(norm(matriz[indices_incognitas[0]])*norm(matriz[1]))
    print(result_coseno)
    #s umatorio = []
    #for i in matriz:
    #   for j in i:
    #         sumatorio[i] = sumatorio[i][j] - media
    





# def distancia_coseno(matriz)



# def distancia_euclidea(matriz)



# def traspuesta(m):
#     matriz_traspuesta = []
#     matriz_traspuesta = np.transpose(m)
#     #print(matriz_traspuesta)
#     return matriz_traspuesta


# menu de las opciones
# metodos de calculo
    # Correlacion de Pearson.
    # Distancia coseno.
    # Distancia Euclidea.
# Numero de vecinos considerado.
# Tipo de prediccion:
    # Prediccion simple.
    # Diferencia con la media

#a = ['1 2 3', '4 5 -', '7 8 9']
#L = lectura_fichero("pruebaGCO.txt")
L = lectura_fichero('pruebaGCO.txt')
print(L) 
correlacion_pearson(L)

print(indices_incognitas)