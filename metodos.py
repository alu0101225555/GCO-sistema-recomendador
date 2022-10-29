import numpy as np
import argparse

#Lee por línea de comandos e imprime
parser = argparse.ArgumentParser(description='Sistema recomedador')
parser.add_argument('-fichL', '--fichero_lectura', type = str, help='Nombre fichero lectura')
args = parser.parse_args()
variables = vars(args)
print(variables)

#Abre el fichero de entrada
fichero = open(args.fichero_lectura, "r")
#Guarda el contenido del fichero e imprime
contenido = []

while(True):
    #contenido.append(fichero.readline())
    linea = fichero.readline()
    if not linea:
        break
    #print(linea.strip())
    contenido.append(linea)
#Cierra el fichero
fichero.close()

#Array que contendrá los filas de los usuarios que no tengan incógnitas
usuarios_comparar = []
#Recorre cada lista de contenido y compruba si no está la incógnita
for lin in contenido:
    if '-' not in lin:
        #print(lin)
        usuarios_comparar.append(lin)

#Convierte a entero la lista
a = ["1", "2", "3"]
print(type(a[0]))
a [:]= list((map(int, a)))
print(type(a[0]))



#def mediaUsuario(usuarios):
    #sum = 0
    #for i in usuarios:
        #sum += i
    #return sum

#mediaUsuario(usuarios_compararInt))
