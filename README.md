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

La métrica elegida. Los posibles valores son:



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
```
Argumentos:
* ```-fichL FICHERO_LECTURA, --fichero_lectura FICHERO_LECTURA```: Nombre del fichero.
* ```-similitud CALCULO_SIMILITUDES, --calculo_similitudes CALCULO_SIMILITUDES```: Opción del método de similitud.
* ```vecinos NUM_VECINOS, --num_vecinos NUM_VECINOS```: Número de vecinos.

Ejemplo de ejecución:
<!-- PONER EL DEFINITIVO -->
```bash
python GCO.py -fichL pruebaGCO.txt -similitud pearson -vecinos 2
```

Para el funcionamiento de la aplicación, se recomienda utilizar la versión 2.7.17 de Python. Ya que no se soporta en versiones superiores.



## 3. SIMILITUD <a name="id3"></a>
La medida de similitud es una función cuyo valor real cuantifica la semejanza entre dos objetos. Esta es utilizada para medir hasta qué punto dos objetos, de acuerdo con los valores de sus atributos (características), son similares.

### 3.1 Correlación de pearson <a name="id4"></a>
Para calcular la correlación de Pearson, creamos una lista global para almacenar las correlaciones de cada incognita de usuario.

Previamente, calculamos una lista que contiene los índices de las incognitas (una lista con el índice de la fila y, otra, la columna de la matriz). En la función, recorremos dicha lista por los índices de la columna.

<!-- HAY QUE REDACTARLO BIEN... -->
En aux guardamos una los valores de la correlación de cada incognita de las filas. Es decir, si tenemos 3 incóginas en la matriz original, tendremos 3 correlaciones de dicho item (?)

Dentro del primer bucle, creamos un iterador donde j empezará desde la fila 0 hasta el número de filas totales de la matriz. Si j es igual a la fila donde se encuentra la incognita, seguimos con la siguiente fila (sino, se haría la correlación de la fila incognita con ella misma). En caso contrario, guardamos en aux la lista de la correlación.
Para el cálculo de la correlación, usamos la función ```np.corrcoef()```, donde indicamos las filas (?) para hallar el cálculo.
Finalmente, en la lista global de la correlación, insertamos la lista con la correlación de cada incognita

```python

```



### 3.2 Distancia Euclídea <a name="id5"></a>
<!-- MISMA IDEA QUE LO ANTERIOR, PERO MAL REDACTADO :/ -->
En esta función, iteramos por fila de los índices de la lista incognita.(?)
Creamos una lista, aux, para almacenar los valores de la distancia Euclídea que calculamos de las filas de cada incognita. Después, guardamos la lista aux en la lista global.

```python

```


<!-- Noelia -->
### 3.3 Distancia Coseno <a name="id6"></a>

## 4. NÚMEROS DE VECINOS <a name="id7"></a>


## 5. PREDICCIÓN <a name="id8"></a>

### 5.1 Predicción simple <a name="id9"></a>


### 5.2 Diferencia con la media <a name="id10"></a>
