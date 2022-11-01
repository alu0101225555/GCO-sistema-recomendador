# Sistemas de recomendación. Métodos de Filtrado Colaborativo

Noelia Ibáñez Silvestre - alu0101225555

Dana Belén Choque Zárate - alu0101328348

# ÍNDICE
- [INTRODUCCIÓN](#id1)
- [FUNCINAMIENTO](#id2)
- [SIMILITUD](#id3)
  - [Correlación de pearson](#id4)
  - [Distancia Euclídea](#id5)
  - [Distancia Coseno](#id6)
- [NÚMERO DE VECINOS](#id7)
- [PREDICCIÓN](#id8)
  - [Predicción simple](#id9)
  - [Diferencia con la media](#id10)



## 1. INTRODUCCIÓN <a name="id1"></a>
Se ha desarrollado una aplicación por línea de comandos que resuelve un sistema de recomendación siguiendo el método de filtrado colaborativo. 



## 2. FUNCIONAMIENTO <a name="id2"></a>
Este programa recibe como entradas el nombre del fichero de extensión txt, el método de similitud, el número de vecinos y la predicción.
Las opciones son:
- Similitud:
  - Correlación de Pearson
  - Distancia coseno
  - Distancia Euclídea
- Número de vecinos considerado
- Tipo de predicción:
  - Predicción simple
  - Diferencia con la media

MODO DE EJECUCIÓN:
```bash
python GCO.py [-h]
              [-fichL FICHERO_LECTURA]
              [-similitud CALCULO_SIMILITUDES]
              [-vecinos NUM_VECINOS]
              [-prediccion TIPO_PREDICCION]
```
Argumentos:
* ```-fichL FICHERO_LECTURA, --fichero_lectura FICHERO_LECTURA```: Nombre del fichero.
* ```-similitud CALCULO_SIMILITUDES, --calculo_similitudes CALCULO_SIMILITUDES```: Opción del método de similitud.
* ```vecinos NUM_VECINOS, --num_vecinos NUM_VECINOS```: Número de vecinos.
* ```-prediccion TIPO_PREDICCION```: Tipo de predicción.

Ejemplo de ejecución:
<!-- PONER EL DEFINITIVO -->
```bash
python GCO.py -fichL [FILE_NAME] -similitud [pearson | euclidea | coseno] -vecinos [NUM_INT] -prediccion [simple | media]
```
```bash
usuario@ubuntu:/mnt/c/Users/uSer/OneDrive/Escritorio/Cuarto/GCO/PE/GCO-sistema-recomendador$ python GCO.py -fichL prueba1.txt -similitud pearson -vecinos 2 -prediccion simple
MATRIZ ORIGINAL
[['5' '3' '4' '4' '-']
 ['3' '1' '2' '3' '3']
 ['4' '3' '4' '3' '5']
 ['3' '3' '1' '5' '4']
 ['1' '5' '5' '2' '1']]
('Los vecinos mas proximos son: ', [[0.8528028654224417, 0.7071067811865475]])
('Resultado opcion similitud elegida:', [[-2, 0.8528028654224417, 0.7071067811865475, 0.0, -0.7921180343813393]])
('Resultado precision simple:', 4.0)

usuario@ubuntu:/mnt/c/Users/uSer/OneDrive/Escritorio/Cuarto/GCO/PE/GCO-sistema-recomendador$ python GCO.py -fichL prueba1.txt -similitud pearson -vecinos 2 -prediccion media
MATRIZ ORIGINAL
[['5' '3' '4' '4' '-']
 ['3' '1' '2' '3' '3']
 ['4' '3' '4' '3' '5']
 ['3' '3' '1' '5' '4']
 ['1' '5' '5' '2' '1']]
('Los vecinos mas proximos son: ', [[0.8528028654224417, 0.7071067811865475]])
('Resultado opcion similitud elegida:', [[-2, 0.8528028654224417, 0.7071067811865475, 0.0, -0.7921180343813393]])
('Resultado precision con media:', [4.6, 4.871979899370592])

```

Para el funcionamiento de la aplicación, se recomienda utilizar la versión 2.7.17 de Python. Ya que no se soporta en versiones superiores.



## 3. SIMILITUD <a name="id3"></a>
La medida de similitud es una función cuyo valor real cuantifica la semejanza entre dos objetos. Esta es utilizada para medir hasta qué punto dos objetos, de acuerdo con los valores de sus atributos (características), son similares.

### 3.1 Correlación de pearson <a name="id4"></a>
Para calcular la correlación de Pearson, creamos una lista global para almacenar las correlaciones de cada incógnita de usuario.

Previamente, calculamos una lista que contiene los índices de las incógnitas (una lista con el índice de la fila y, otra, la columna de la matriz). En la función, recorremos dicha lista por los índices de la columna.
En la lista aux guardamos una los valores de la correlación de cada incógnita de las filas. Es decir, si tenemos 3 incógnitas en la matriz original, tendremos 3 correlaciones de dicho item.

Dentro del primer bucle, creamos un iterador donde _j_ empezará desde la fila 0 hasta el número de filas totales de la matriz. Si _j_ es igual a la fila donde se encuentra la incógnita, seguimos con la siguiente fila y en la matriz, insertamos un valor -2. En caso contrario, guardamos en aux la lista de la correlación.

Para el cálculo de la correlación, usamos la función ```np.corrcoef()```.
Finalmente, en la lista global de la correlación, insertamos la lista con la correlación de cada incógnita.

```python
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
```



### 3.2 Distancia Euclídea <a name="id5"></a>
Esta función, recibe como parámetro la matriz de valores. En dicha función, tiene la misma idea de iteración que la función Euclídea, sin embargo, utilizamos la función ```np.linalg.norm()``` para el cálculo de la Distancia Euclídea.

```python
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
```


<!-- Noelia -->
### 3.3 Distancia Coseno <a name="id6"></a>
Creamos el método ```distancia_coseno``` que recibe la matriz como parámetro. A continuación, vamos recorriendo la lista de los índices de las incógnitas y creamos un aux; a su vez, recorremos la matriz y comparamos si la posición de la actual de la matriz coincide con la posición de la incógnita, si es así introducimos un -2 en dicha posición, ya que nunca se podrá coger dicho valor y esto se hace para que la lista tenga la misma cantidad de elementos que la original. En caso contrario calculamos la distancia coseno haciendo uso de la función de la librería numpy ```np.dot(matriz[i], matriz[j])/(norm(matriz[i])*norm(matriz[j]))``` y lo introducmos en la variable aux para, al final, crear una lista de listas que contengas las distancias cosenos.

```python
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
```

## 4. NÚMEROS DE VECINOS <a name="id7"></a>
Para la función ```vecino``` le pasamos la lista de similitudes calculadas con el método elegido y el número de vecinos que desea coger el usuario. Además, debemos crear una variable llamada *lista_cortada_vecinos* que será una lista de listas para la lista de la cantidad de vecinos más próximos elegidos para cada usuario. A continuación, comprobamos que el numero de vecinos introducidos por consola son mayor que 0 y menor que el número de filas (personas que forman la matriz) y, si se cumplen las condiciones, recorremos la lista de similitudes, creamos una variable auxiliar *lista_ordenada* que ordenará la lista de similitudes de mayor a menor para después cortarla hasta el número de vecinos establecidos por el usuario *lista_ordenada[0:n_vecinos]* para después introducirlos finalmente en la lista final *lista_cortada_vecinos* que retornará la función.

```python
def vecinos(lista, n_vecinos):
    lista_cortada_vecinos = []

    if (n_vecinos == 0) or (n_vecinos < len(lista)):
        print("El numero de vecino tiene que ser mayor que 0 y menor que el numero de filas")
    else:
        for i in lista:
            lista_ordenada = sorted(i, reverse=True)
            lista_vecinos = lista_ordenada[0:n_vecinos]
            lista_cortada_vecinos.append(lista_vecinos)

    return lista_cortada_vecinos
```

## 5. PREDICCIÓN <a name="id8"></a>

### 5.1 Predicción simple <a name="id9"></a>
En la función ```predicSimple``` necesitamos pasarle la lista con las similitudes de los vecinos elegidos *lista_cortada_vecinos_ordenada* y la lista general de similitudes *lista_desordenada*.
A continuación, comparamos la *lista_cortada_vecinos_ordenada* y la lista general desordenada para obtener los índices de los usuarios.

```python
    indices_item_iguales_listas = []
    for elemento_array in lista_cortada_vecinos_ordenada:
        for item in elemento_array:
            aux_indice = np.where(lista_desordenada == item)
            
            indices_item_iguales_listas.append(aux_indice[1][0])
```
Una vez tenemos los índices, convertimos la matriz en dataframe para poder extraer de manera más fácil los valores. A medida que recorremos el dataframe, comprobamos si el índice de la incógnita coincide con los índices de los usuarios que queremos y extraemos el valor, guardándolas en *aux_valores_usuarios*. 

```python
    df = pd.DataFrame(matriz_copia)
    aux = []
    for j in indices_incognitas[1]: 
        for i in range(len(df)):
            aux = df.iloc[i,j]

    aux_valores_usuarios = []
    for i in indices_item_iguales_listas:
        for j in indices_incognitas[1]:
            aux_valores_usuarios.append(df.iloc[i,j])
```

Por último, hacemos los cálculos correspondientes con los valores obtenidos:

```python
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
```

### 5.2 Diferencia con la media <a name="id10"></a>
A la función ```predicMedia()``` le pasamos la lista de similitud de los vacinos, la lista de similitud original y la matriz que contiene los valores de las filas sin contar la columna de las incógnitas.

Calculamos los índices de los usuarios y lo guardamos en una lista. Convertimos la columna de las incógnitas en dataframe para obtener la valoración de los items de dicha columna.

Después, calculamos las medias de las filas de los usuarios de la lista de vecinos (incluyendo las valoraciones de la columna de la incógnita). Finalemte, calculamos la predicción con media utilizando las listas que hemos hallado anteriormente.

```python
def predicMedia(lista_cortada_vecinos_ordenada, lista_desordenada, matriz):

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

    aux_valoracion_item_usuario = []
    aux_media_usuarios = []
    media_usuarios = []
    valoracion_item_usuario = []
    for fila in indices_item_iguales_listas:
        for j in indices_incognitas[1]:
            aux_fila = []
            aux_fila = matriz[fila].copy()
            aux_fila = np.append(aux_fila, df.iloc[fila,j])
            aux_valoracion_item_usuario.append(df.iloc[fila,j])
            aux_media_usuarios.append(media(aux_fila))
    
    sumatorio = 0
    sumatorioDenominador = 0
    lista_prediccion_con_media = []
    for lista in lista_cortada_vecinos_ordenada:
        for k in range(len(aux_media_usuarios)):
            multiplicacion = lista[k] * (aux_valoracion_item_usuario[k] - aux_media_usuarios[k])
            sumatorio = sumatorio + multiplicacion
            if(lista[k] < 0):
                sumatorioDenominador = abs(sumatorioDenominador + lista[k])
            else:
                sumatorioDenominador = sumatorioDenominador + lista[k]
            lista_prediccion_con_media.append(media(matriz[indices_incognitas[0]]) + (sumatorio/sumatorioDenominador))
    print("Resultado precision con media:", lista_prediccion_con_media)

```

El problema que nos hemos encontrado en esta función, es que sólo funciona para [ejemplo1.txt](https://github.com/alu0101225555/GCO-sistema-recomendador/blob/50e9d117cd3327f7808d2da7085507f695bece7c/prueba1.txt).