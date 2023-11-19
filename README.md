# Proyecto de Ramificación y Acotación

Este proyecto ha sido realizado por Daniel Talavera Hernández y María Alonso León como parte de la asignatura de Fundamentos de los Sistemas Inteligentes de la Universidad de Las Palmas de Gran Canaria. El objetivo principal del proyecto es implementar y analizar el algoritmo de Ramificación y Acotación en Python. Se han realizado varias implementaciones y se han introducido mejoras para medir y comparar su rendimiento.

## Implementaciones

### Clases Fifo

Se han añadido dos clases `myFifoQueue` y `myFifoQueue_with_sub` para la realización del algoritmo de Ramificación y Acotación sin y con subestimación. Estas clases están basadas en la estructura de datos de cola (FIFO) y se utilizan para explorar el espacio de búsqueda de manera eficiente.

En cuanto a la subestimación es importante destacar que la heurística seguida es la distancia en línea recta entre el nodo actual y el destino.

Es importante destacar que en estas clases se han añadido dos métodos extras `printStats()` y `printQuality()`. En el primero de ellos aparecen las siguientes estadísticas:

- Nodos vistados.
- Nodos no vistados.
- Nodos que han estado alguna vez en el fringe.
- Nodos generados.
- Nodos podados.

Estas estadísticas nos ayudan a tener una visión más exhaustiva del funcionamiento del código y el algoritmo.

Por su parte, el segundo método `printQuality()` muestra la calidad para para velocidad y memoria del algoritmo. En cuanto al de la solcuión, ya que este es común para con y sin subestimación se añadió en el fichero `run.py`.

### Funciones de Búsqueda

Se han creado dos funciones adicionales, `branch_and_bound_search` y `branch_and_bound_search_with_sub`, que utilizan la función `graph_search()` junto con la clase `Fifo` correspondiente para implementar los algoritmos de Ramificación y Acotación con y sin subestimación.

## Uso

Para ejecutar los algoritmos de Ramificación y Acotación, se puede utilizar las siguientes funciones:

- `branch_and_bound_search(problem)`: Implementa el algoritmo de Ramificación y Acotación sin subestimación.

- `branch_and_bound_search_with_sub(problem)`: Implementa el algoritmo de Ramificación y Acotación con subestimación.

## Resultados

El proyecto ha sido exitoso en la implementación y análisis de los algoritmos de Ramificación y Acotación. Se han obtenido resultados prometedores en términos de eficiencia y rendimiento.

No obstante, se debe destacar que aunque el algoritmo de Ramificación y Acotación sin subestimación es eficiente y encuentra soluciones óptimas al problema; durante la exploración del espacio de búsqueda, puede visitar un número significativamente mayor de nodos. Esto se debe a que no tiene información adicional para priorizar la expansión de nodos prometedores, lo que resulta en una exploración exhaustiva del espacio. 

Por su parte, el algoritmo de Ramificación y Acotación con subestimación utiliza una función de subestimación (heurística) que proporciona una estimación del costo restante para llegar a una solución. Esto permite al algoritmo enfocarse en nodos que tienen el potencial de conducir a soluciones más óptimas. Como resultado, el número de nodos visitados con este enfoque es significativamente menor que en el algoritmo sin subestimación.

La razón detrás de esta diferencia radica en la capacidad del algoritmo de Ramificación y Acotación con Sub para evitar explorar caminos que se estima que no conducen a una solución óptima. Esto hace que el algoritmo con subestimación sea más eficiente en términos de tiempo y recursos computacionales, lo que es especialmente beneficioso en problemas con espacios de búsqueda grandes y complejos.

Por último, cabe destacar que al observar las formas de medición de la calidad (velocidad, memoria, y longitud de la solución) se ha podido comprobar que 