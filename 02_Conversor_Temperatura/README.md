# Conversor de Temperatura

Programa de consola desarrollado en Python que convierte temperaturas entre grados Celsius y Fahrenheit.

## Funciones

- Convertir Celsius a Fahrenheit.
- Convertir Fahrenheit a Celsius.
- Validar entradas incorrectas.
- Realizar varias conversiones sin reiniciar el programa.
- Mostrar resultados con dos decimales.

## Requisitos

- Python 3

No necesita librerías externas.

## Cómo ejecutar el proyecto

Abre una terminal dentro de `02_Conversor_Temperatura` y ejecuta:

```bash
python conversor.py
```

En Windows también puedes utilizar:

```bash
py conversor.py
```

## Fórmulas utilizadas

Para convertir Celsius a Fahrenheit:

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

Para convertir Fahrenheit a Celsius:

```text
Celsius = (Fahrenheit - 32) × 5 / 9
```

## Ejemplo

```text
---- CONVERSOR DE TEMPERATURA ----
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
3. Salir

Elige una opción (1-3): 1
Escribe la temperatura en grados Celsius: 100
100.00 °C equivalen a 212.00 °F
```

## Pruebas realizadas

```text
0 °C = 32 °F
100 °C = 212 °F
32 °F = 0 °C
-40 °C = -40 °F
```

## Conceptos practicados

- Funciones
- Condicionales
- Bucles
- Conversión de tipos de datos
- Manejo de errores con `try` y `except`
- Fórmulas matemáticas
- Formato de números decimales con f-strings

## Autor

Proyecto creado por Marcelo como parte de su portafolio de aprendizaje de Python.