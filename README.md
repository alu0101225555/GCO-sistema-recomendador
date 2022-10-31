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
<!-- FALTA... -->



### 3.2 Distancia Euclídea <a name="id5"></a>


<!-- Noelia -->
### 3.3 Distancia Coseno <a name="id6"></a>

## 4. NÚMEROS DE VECINOS <a name="id7"></a>


## 5. PREDICCIÓN <a name="id8"></a>

### 5.1 Predicción simple <a name="id9"></a>


### 5.2 Diferencia con la media <a name="id10"></a>
