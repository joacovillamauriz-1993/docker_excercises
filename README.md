# Reto notas Python y Docker — Grupo 1

Script en Python (`notas.py`) que recorre una lista de alumnos, indica si cada uno está aprobado o suspenso y muestra el total, el número de aprobados/suspensos y la media de la clase. Se ejecuta dentro de un contenedor Docker.

## Integrantes

- JOAQUIN_VILLALOBOS (MDIA)
- IGNACIO-PINAZO (MDIA)
- RICARDO_ROMAN (MDES)

## Contenido del repositorio

- `notas.py`: script principal.
- `Dockerfile`: imagen basada en `python:3.12-slim` (el script requiere Python 3.12+ por el uso de comillas anidadas en f-strings).
- `README.md`: este documento.

## Construir la imagen

```bash
docker build -t notas-python .
```

## Ejecutar el contenedor

```bash
docker run --rm notas-python
```

## Salida esperada

```
ANA: 8.5 -> Aprobad@ 
LUIS: 4.0 -> Suspens@ 
MARTA: 7.0 -> Aprobad@ 
PABLO: 3.5 -> Suspens@ 
SARA: 9.0 -> Aprobad@ 

Total estudiantes: 5
Estudiantes aprobadxs: 3
Estudiantes suspensxs: 2
Media de la clase: 6.4
```

## Pull request

Enlace a la pull request de `develop` a `main`: [[text](https://github.com/joacovillamauriz-1993/docker_excercises/pull/2)]
