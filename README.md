# localizadorGrafos

El objetivo de este proyecto, fue aplicar algunos de los conocimientos adquiridos en la materia de algoritmos para dar solución al problema de la ubicación óptima.
En este problema, tomamos un grafo, que es una representación de un mapa de x zona, y el objetivo, sera obtener el mejor punto de ubicación dentro del grafor considerando el lugar más cercano a todos los demas, o el más lejano.

Planteamos que la solución más optima es calcular las distancias totales de la red,
mediante la obtención de todos los caminos mínimos del grafo, o en este caso, del
mapa en cuestión, en una calle hay excesiva competencia, planteamos que lo
óptimo para sobrevivir en el mercado es cambiar de ubicación el establecimiento,
todo esto mediante la ponderación de cada nodo, los pesos que tendrán asociados
las aristas no necesariamente representan solamente una distancia, también
pueden representar el nivel de competencia entre la zona, o si por cuestiones de
seguridad, no es muy bueno el nodo (ubicación del mapa)

Para más información del proyecto, o su fundamento matemático, consultar el reporte anexado en este repositorio.

Resultados:

![image](https://github.com/AngelVelascoH/localizadorGrafos/assets/86260733/4cdc30c3-e11f-46f1-bb3a-977d80da8b30)

**Se despliega el grafo seleccionado**

![image](https://github.com/AngelVelascoH/localizadorGrafos/assets/86260733/aebb2ea6-17a4-4010-83ec-3001a88cea8f)

**obtenemos el punto mas cercano de la red**

![image](https://github.com/AngelVelascoH/localizadorGrafos/assets/86260733/8132f8f0-3103-489e-b30a-7fceb2d3cd60)

**ahora, el más lejano**

![image](https://github.com/AngelVelascoH/localizadorGrafos/assets/86260733/e7638836-0999-47ca-baa5-f7055906f421)

Este programa es de ayuda para la localización óptima, lo unico necesario, es obtener un grafo del mapá a analizar en formato gml.





