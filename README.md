# Buda_ShortPath
En la red de metro algunas estaciones pueden tener un color asociado (Rojo o Verde) que indica que un tren exprés de color Verde pasará solo por estaciones sin color o Verde, y un tren exprés de color Rojo pasará solo por estaciones sin color o Roja.
```console
Usage: shortPathFinal.py [OPTIONS]

Options:
  --filename TEXT     Network file, in json format [required]
  --origin TEXT       Source node of the network  [required]
  --destination TEXT  Destination node of the network  [required]
  --color TEXT        Train color, green, red [dont add for colorless]
  --help              Show this message and exit.
  ```
  
  
  # Unit test
  Test automático de las partes mas importantes
  test_0: Prueba del método Mapa, el cual produce una matriz con los caminos y distancias posibles para utilizar en djikstra
  test_1: Prueba que el método (utilizado por djikstra) de mínima distancia funcione correctamente
  test_2: Prueba que el algoritmo de Djikstra entrege el resultado correcto
  
  Ejemplo de una prueba exitosa:
```console
python.exe .\automaticTest.py

Start Mapa test

.
Start minDistance test

.
Start djikstra test

.
----------------------------------------------------------------------
Ran 3 tests in 0.006s

OK
```
