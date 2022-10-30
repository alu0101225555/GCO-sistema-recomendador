#  PDF describiendo el analisis realizado en varios ejemplos y las conclusiones extraidas.
import numpy as np
from numpy import mean
import pandas as pd
import argparse
from numpy.linalg import norm

# para ejecutar de momento (solo leyendo el fichero de entrada): python3 GCO.py -fichL pruebaGCO.txt 
from numpy.core.fromnumeric import transpose

#Lee por linea de comandos e imprime
parser = argparse.ArgumentParser(description='Sistema Recomedador')
parser.add_argument('-fichL', '--fichero_lectura', type = str, help='Nombre fichero lectura')
parser.add_argument('-similitud', '--calculo_similitudes', type = str, help='Opcion de metodo de calculo de similitud')
parser.add_argument('-vecinos', '--num_vecinos', type = int, help='Numero de vecinos')
# parser.add_argument('-prediccion', '--tipo_prediccion', type = str, help='Tipo de prediccion')

args = parser.parse_args()
variables = vars(args)
#print(variables)

indices_incognitas = []
lista_pearson_correlation = []
lista_distancia_euclidea = []
lista_distancia_coseno = []
matriz_copia = []

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

#----------------------------------
    # 1.1 guardar los valores de las columnas eliminadas para calcular la prediciones
    global matriz_copia
    matriz_copia = np.zeros((len(A), len(A[0])), dtype=int)
    print(matriz_copia)

   
    #IDEA: Dentro del bucle, copiar valores de aux en la posiciones de las fila de la copia in convertir
    # los valores en int directamente. Aux se itera por columnas y copia_matriz por filas (mismo iterador)
    # print(array)
    for ing in indices_incognitas[1]:
        fila = 0
        aux = A[:,ing]
        # print(aux)
        while (fila < len(A[0])):
            if (aux[fila] == '-'):
                matriz_copia[fila][ing] = -1 #-1 indica que es la incognita pq no se puede poner como None
                fila = fila + 1
            else:
                matriz_copia[fila][ing] = int(aux[fila])
                # print(matriz_copia[fila][ing])
                fila = fila + 1
    print("MATRIZ COPIA", matriz_copia) #la matriz_copia contiene una maatriz inicializada a 0 con las columnas que contienen la incognita copiadas de la matriz original 


#--------------------------------             
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
    # media = np.mean(matriz, axis=1)
    # print(media)

    #creacion dataframe
    #df_pearson = pd.DataFrame()

    #bucle que recorre indices_incognitas
    global lista_pearson_correlation
    for i in indices_incognitas[0]:
        j = 0
        aux = []
        # print("INCOGNITA CORRELACION PEARSON: ", i)  
        
        while j < len(matriz):
            if (j == i):
                j = j + 1
            else:
                # print(matriz[i])
                # print(matriz[j])
                #corr_data = np.corrcoef(matriz[i], matriz[j])[1,0]
                # print(corr_data)
                aux.append(np.corrcoef(matriz[i], matriz[j])[1,0])
                # print(aux)
                # print(lista_pearson_correlation)
                # guardamos en dataframe
                # df_pearson = df_pearson.append(corr_data, ignore_index=True)
                j = j + 1

        lista_pearson_correlation.append(aux)
        return lista_pearson_correlation

    # corr_data = np.corrcoef(matriz[indices_incognitas[0]], matriz[1])[1,0]
    # print(corr_data)
    
    # dist_euclide = np.linalg.norm(matriz[indices_incognitas[0]] - matriz[1])
    # print(dist_euclide)
    
    # result_coseno = np.dot(matriz[indices_incognitas[0]], matriz[1])/(norm(matriz[indices_incognitas[0]])*norm(matriz[1]))
    # print(result_coseno)
    #s umatorio = []
    #for i in matriz:
    #   for j in i:
    #         sumatorio[i] = sumatorio[i][j] - media
    
def distancia_euclidea(matriz):
    for i in indices_incognitas[0]:
        j = 0
        aux = []
        # print("INCOGNITA DISTANCIA EUCLIDES: ", i)  
        
        while j < len(matriz):
            if (j == i):
                j = j + 1
            else:
                # print(matriz[i])
                # print(matriz[j])
                # dist_euclide = np.linalg.norm(matriz[i] - matriz[j])
                # print(dist_euclide)
                aux.append(np.linalg.norm(matriz[i] - matriz[j]))
                # corr_data = np.corrcoef(matriz[i], matriz[j])[1,0]
                # print(corr_data)
                j = j + 1
        lista_distancia_euclidea.append(aux)
    return lista_distancia_euclidea



def distancia_coseno(matriz):
    for i in indices_incognitas[0]:
        j = 0
        aux = []
        # print("INCOGNITA DISTANCIA COSENO: ", i)  
        
        while j < len(matriz):
            if (j == i):
                j = j + 1
            else:
                # print(matriz[i])
                # print(matriz[j])
                # result_coseno = np.dot(matriz[i], matriz[j])/(norm(matriz[i])*norm(matriz[j]))
                aux.append(np.dot(matriz[i], matriz[j])/(norm(matriz[i])*norm(matriz[j])))
                # print(result_coseno)
                # dist_euclide = np.linalg.norm(matriz[i] - matriz[j])
                # print(dist_euclide)
                # corr_data = np.corrcoef(matriz[i], matriz[j])[1,0]
                # print(corr_data)
                j = j + 1
        lista_distancia_coseno.append(aux)

    # orde_coseno = sorted(lista_distancia_coseno)
    # print("Lista ordenada coseno:", orde_coseno)

    return lista_distancia_coseno
    

def vecinos(lista, n_vecinos):
    lista_cortada_vecinos = [] #aux es una lista de listas que contiene las similitudes entre vecinos "cortadas"
    #comprobar num vecinos cuando el usuario inserte parametros al principio
    if (n_vecinos == 0) or (n_vecinos < len(lista)):
        print("El numero de vecino tiene que ser mayor que 0 y menor que el numero de filas")
    else:
        for i in lista:
            lista_ordenada = sorted(i, reverse=True)
            # print("Lista ordenada:", lista_ordenada)
            lista_vecinos = lista_ordenada[0:n_vecinos]
            lista_cortada_vecinos.append(lista_vecinos)
            # print("Lista cortada:", aux)
    return lista_cortada_vecinos

# def prediccion_simple(lista_cortada_vecinos_ordenada,  lista_desordenada):
# #   IDEA: hacer la media de las incognitas (media de la fila sin el item de la columna incognita)
# #         hacer las medias de las demas filas contando la columna del item de la columna incognita

# #         Comparamos lista_ordenada con desordenada para obtener los indices de los usuarios
#     # for elemento_array in lista_cortada_vecinos_ordenada:
#     #     for item in elemento_array:
#     #         for elemento_array2 in lista_desordenada:
#     #             for item2 in elemento_array2:
#     #                 if item == item2:
#     #                     print(item)
#     #                     print("indices: ", np.where(lista_desordenada == item2))
    
#     # Comparamos lista_ordenada con desordenada para obtener los indices de los usuarios
#     indices_item_iguales_listas = []
#     for elemento_array in lista_cortada_vecinos_ordenada:
#         for item in elemento_array:
#             # indices_item_iguales_listas contiene los indices de los items que son iguales entre las
#             # listas_cortada_vecinos_ordenada y la lista_desordenada que contiene todas las similitudes
#             aux_indice = np.where(lista_desordenada == item)
            
#             indices_item_iguales_listas.append(aux_indice[1][0]) #son las columnas de los items iguales
#             print(aux_indice[1][0])
#             # print(indices_incognitas[1][0])
#             # obtener el valor de la matriz copia que esta en ese indice
#             print(matriz_copia[:,indices_incognitas[1][0]][1 + aux_indice[1][0]])
#             # print(matriz_copia[:,indices_item_iguales_listas[0]])
#             # print("indices: ", indices_item_iguales_listas)
#     # print("indices: ", indices_item_iguales_listas)
                        
#     # extraemos los valores de la posicion de la matriz






# menu de las opciones
def main():

    fichero = lectura_fichero(args.fichero_lectura)
    opcion = []
    # metodos de calculo
    # Correlacion de Pearson.
    if (args.calculo_similitudes == 'pearson'):
        opcion = correlacion_pearson(fichero)
    # Distancia coseno.
    elif (args.calculo_similitudes == 'distancia euclidea') or (args.calculo_similitudes == 'euclidea'):
        opcion = distancia_euclidea(fichero)  
    # Distancia Euclidea.
    elif (args.calculo_similitudes == 'distancia coseno') or (args.calculo_similitudes == 'coseno'):
        opcion = distancia_coseno(fichero)
    else:
        print("ERROR en la introduccion del parametro similitud")
    
    # Numero de vecinos considerado.
    if (args.num_vecinos > 0) and (args.num_vecinos < len(matriz_copia)):
        vecinos1 = vecinos(opcion, args.num_vecinos)
        print("Los vecinos mas proximos son: ", vecinos1)
    else:
        print("ERROR. El numero de vecinos tiene que ser mayor que 0 e inferior las filas de la matriz")

    print("Resultado opcion similitud elegida:", opcion)
    
    # Tipo de prediccion:
    # Prediccion simple.
    # Diferencia con la media
    
    
    # CP = correlacion_pearson(L)
    # DE = distancia_euclidea(L)
    # DC = distancia_coseno(L)
    # V = vecinos(DE, 2)
    # print("Lista cortada:", V)

    # print("Lista correlaciones de pearson:", lista_pearson_correlation)
    # print("Lista distancia euclideas:", lista_distancia_euclidea)
    # print("Lista distancia coseno:", lista_distancia_coseno)

    # print("Indices incognitas:", indices_incognitas)

    # prediccion_simple(V, DE)
    
main()