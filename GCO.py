import numpy as np
import argparse

from numpy.core.fromnumeric import transpose

#Lee por línea de comandos e imprime
parser = argparse.ArgumentParser(description='Sistema recomedador')
parser.add_argument('-fichL', '--fichero_lectura', type = str, help='Nombre fichero lectura')
args = parser.parse_args()
variables = vars(args)
#print(variables)

# Lectura fichero: va leyendo la matriz linea por linea, elimina los saltos de linea y
# los introduce en la lista matriz_fichero
def lectura_fichero(nombre_fichero):
    fich_entrada = open(nombre_fichero, 'r')
    matriz_fichero = []
    for linea in fich_entrada:
        linea = linea.rstrip('\n')
        matriz_fichero.append(linea)

    #print(type(matriz_fichero[0]))
    return matriz_fichero
    #fich_entrada.close()  

# Crea una copia de la matriz
def copy(m):
    result = []
    for f in m:
        result.append(f[:])
    return result

def traspuesta(m):
    matriz_traspuesta = []
    matriz_traspuesta = np.transpose(m)
    #print(matriz_traspuesta)
    return matriz_traspuesta

# Convierte lista a enteros: recorremos filas y comprobamos si se encuentra el elemento '-'
# si no está, convertimos cada elemento en un int y lo pasamos a una 
# nueva lista result_filas 
#def conv_int(m):
#    result_filas = []
#    for row in m:
#        if ('-' not in row):
#            for elem in row:
#                aux = int(elem)
#                result_filas.append(aux)
#    
#    return result_filas

# Extrae las filas sin incognita y las introduce en result[]
def extraccion_filas(m):
    result = []
    print (m)
    for i in m:
        if ('-' not in i):
            result.append(i)
            #print(i)
    #print(result)
    return result

# Convierte lista a enteros: recorremos filas y comprobamos si se encuentra el elemento '-'
# si no está, convertimos cada elemento en un int y lo pasamos a una 
# nueva lista enteros
def conv_int2(m):
    enteros = []

    for i in m:
        lista = []
        for elemt in i:
            if elemt != ' ':
                aux = int(elemt)
                lista.append(aux)
        enteros.append(lista)
    return enteros

def extraccion_columna(m):
    result = []

    # esto lo que hace es pasar la lista a lista de vectores [[1,2,3], [4,5,6]]
    for i in m:
        lista = []
        if i != ' ':
            lista.append(i)
        result.append(lista)
    print("lista de vectores", result)
    #

    #traspuesta
        

    # esto lo que hace es ir recorriendo la matriz traspuesta y extraer la fila con '-' quedándonos con las otras en resultado_final
    resultado_final = []
    for i in result:
        for j in i:
            if ('-' not in j) & (j != ' '):
                resultado_final.append(j)

    return resultado_final
        

#a = ['1 2 3', '4 5 -', '7 8 9']
L = lectura_fichero("pruebaGCO.txt")

E =extraccion_columna(L)
print(E)

#B = extraccion_filas(L)
#C = conv_int2(E)
#print(C)
#print(type(C[0][2])) #-> para acceder C[fila][columna]

#D = traspuesta(L)
#print(D)
#C = traspuesta(B)
#print(C)
