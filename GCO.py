import numpy as np
from numpy import mean
import pandas as pd
import argparse
from numpy.linalg import norm
from numpy.core.fromnumeric import transpose

# Lectura por linea de comandos e imprime
parser = argparse.ArgumentParser(description='Sistema Recomedador')
parser.add_argument('-fichL', '--fichero_lectura', type = str, help='Nombre fichero lectura')
parser.add_argument('-similitud', '--calculo_similitudes', type = str, help='Opcion de metodo de calculo de similitud')
parser.add_argument('-vecinos', '--num_vecinos', type = int, help='Numero de vecinos')
# parser.add_argument('-prediccion', '--tipo_prediccion', type = str, help='Tipo de prediccion')

args = parser.parse_args()
variables = vars(args)

indices_incognitas = []
lista_pearson_correlation = []
lista_distancia_euclidea = []
lista_distancia_coseno = []
# la matriz_copia contiene la matriz inicializada a 0 con las columnas que contienen la incognita copiadas de la matriz original 
matriz_copia = []



def lectura_fichero(nombre_fichero):

    A = np.loadtxt(nombre_fichero, dtype='S') #'S' trata el dato como numero
    print("MATRIZ ORIGINAL")
    print(A)
    # Localizamos las incognitas
    global indices_incognitas # indicamos que vamos a modificar la variable global
    indices_incognitas = np.where(A == '-')

    # Guardarmos los valores de las columnas eliminadas para calcular la prediciones
    global matriz_copia
    matriz_copia = np.zeros((len(A), len(A[0])), dtype=int)
   
    #IDEA: Dentro del bucle, copiar valores de aux en la posiciones de las fila de la copia in convertir
    # los valores en int directamente. Aux se itera por columnas y copia_matriz por filas (mismo iterador)
    # print(array)
    for ing in indices_incognitas[1]:
        fila = 0
        aux = A[:,ing]
        while (fila < len(A[0])):
            if (aux[fila] == '-'):
                matriz_copia[fila][ing] = -1 #-1 indica que es la incognita pq no se puede poner como None
                fila = fila + 1
            else:
                matriz_copia[fila][ing] = int(aux[fila])
                fila = fila + 1

    # Eliminamos las columnas que contengan las incognitas
    # axis = 1 indica que haga la operacion por columnas
    A1 = np.delete(A, indices_incognitas[1], axis=1)
    # Pasar la matriz a entero
    # print("MATRIZ CON COLUMNAS ELIMINADAS:")
    # convierte la matriz string a matriz int
    A2 = A1.astype(int)
    # print(A2)

    return A2



def correlacion_pearson(matriz):

    global lista_pearson_correlation
    for i in indices_incognitas[0]:
        j = 0
        aux = []
        
        while j < len(matriz):
            if (j == i):
                j = j + 1
                aux.append(-2)
            else:
                aux.append(np.corrcoef(matriz[i], matriz[j])[1,0])
                j = j + 1

        lista_pearson_correlation.append(aux)

    return lista_pearson_correlation


    
def distancia_euclidea(matriz):

    for i in indices_incognitas[0]:
        j = 0
        aux = []
        
        while j < len(matriz):
            if (j == i):
                j = j + 1
                aux.append(-2)
            else:
                aux.append(np.linalg.norm(matriz[i] - matriz[j]))
                j = j + 1
        lista_distancia_euclidea.append(aux)

    return lista_distancia_euclidea



def distancia_coseno(matriz):

    for i in indices_incognitas[0]:
        j = 0
        aux = []
        
        while j < len(matriz):
            if (j == i):
                j = j + 1
                aux.append(-2)
            else:
                aux.append(np.dot(matriz[i], matriz[j])/(norm(matriz[i])*norm(matriz[j])))
                j = j + 1
        lista_distancia_coseno.append(aux)

    return lista_distancia_coseno
    


def vecinos(lista, n_vecinos):
    lista_cortada_vecinos = []
    #comprobar num vecinos cuando el usuario inserte parametros al principio
    if (n_vecinos == 0) or (n_vecinos < len(lista)):
        print("El numero de vecino tiene que ser mayor que 0 y menor que el numero de filas")
    else:
        for i in lista:
            lista_ordenada = sorted(i, reverse=True)
            lista_vecinos = lista_ordenada[0:n_vecinos]
            lista_cortada_vecinos.append(lista_vecinos)

    return lista_cortada_vecinos



def predicSimple(lista_cortada_vecinos_ordenada, lista_desordenada):

    #Comparamos lista_ordenada con desordenada para obtener los indices de los usuarios
    indices_item_iguales_listas = []
    for elemento_array in lista_cortada_vecinos_ordenada:
        for item in elemento_array:
            aux_indice = np.where(lista_desordenada == item)          
            indices_item_iguales_listas.append(aux_indice[1][0]) #son las columnas de los items iguales

    # dataframe para sacar los valores de la columna incognita
    df = pd.DataFrame(matriz_copia)
    aux = []
    for j in indices_incognitas[1]: 
        for i in range(len(df)):
            aux = df.iloc[i,j]

    aux_valores_usuarios = []
    for i in indices_item_iguales_listas:
        for j in indices_incognitas[1]:
            aux_valores_usuarios.append(df.iloc[i,j])

    sumatorio = 0
    sumatorioDenominador = 0
    for i in lista_cortada_vecinos_ordenada:
        for elemento in i:
          for j in aux_valores_usuarios:
            multiplicacion = elemento * j
            sumatorio = sumatorio + multiplicacion
            if(elemento < 0):
                sumatorioDenominador = abs(sumatorioDenominador + elemento)
            else:
                sumatorioDenominador = sumatorioDenominador + elemento
    
    resultadoSimple = sumatorio/sumatorioDenominador
    print("Resultado precision simple:", resultadoSimple)




def media(lista):
    x = np.mean(lista)
    return x



def predicMedia(lista_cortada_vecinos_ordenada, lista_desordenada):

    # Comparamos lista_ordenada con desordenada para obtener los indices de los usuarios
    indices_item_iguales_listas = []
    for elemento_array in lista_cortada_vecinos_ordenada:
        for item in elemento_array:
            aux_indice = np.where(lista_desordenada == item)            
            indices_item_iguales_listas.append(aux_indice[1][0]) #son las columnas de los items iguales

    # dataframe para sacar los valores de la columna incognita
    df = pd.DataFrame(matriz_copia)
    aux = []
    for j in indices_incognitas[1]: 
        for i in range(len(df)):
            aux = df.iloc[i,j]

    aux_valores_usuarios = []
    for i in indices_item_iguales_listas:
        for j in indices_incognitas[1]:
            aux_valores_usuarios.append(df.iloc[i,j])
    # print("Valores usuarios", aux_valores_usuarios)

    medias_vecinos = []
    for i in aux_valores_usuarios:
        medias_vecinos.append(media(i))
    print("Medias medias", medias_vecinos)
    
    sumatorio = 0
    sumatorioDenominador = 0
    for i in lista_cortada_vecinos_ordenada:
        for elemento in i:
          for j in aux_valores_usuarios:
              for k in medias_vecinos:
                multiplicacion = elemento + (j*k)
                sumatorio = sumatorio + multiplicacion
                if(elemento < 0):
                    sumatorioDenominador = abs(sumatorioDenominador + elemento)
                else:
                    sumatorioDenominador = sumatorioDenominador + elemento

    resultadoSimple = sumatorio/sumatorioDenominador
    print("Resultado precision con media:", resultadoSimple)



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
    predicSimple(vecinos1, opcion)
    # Diferencia con la media
    predicMedia(vecinos1, opcion)

    
main()