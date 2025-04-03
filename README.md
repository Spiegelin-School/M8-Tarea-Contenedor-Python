## ¿Qué hace?
#### Objetivo
Levantar un contenedor de Docker que ejecute el script de python.

#### Script de Python
- Se simulan 90 minutos, alternando el turno de cada equipo.
- Para cada minuto se genera un número aleatorio entre 1 y 350.
- Dependiendo del rango en el que caiga el número, se determina si el disparo es desviado, atajado o si resulta en algún tipo de gol (de cabeza, penal o con el pie). En caso de gol se actualiza el marcador.
- Se imprime un resumen minuto a minuto y el marcador final.

## ¿Cómo correrlo?
1. Construye la imagen Docker.
```zsh
docker build -t sim .
```

2. Ejecuta el contenedor.
```zsh
docker run --rm simulador-futbol
```
