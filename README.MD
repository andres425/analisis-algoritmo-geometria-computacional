# Geometría computacional: navegación de robots y detección de intersecciones

Autor: Andrés — Ingeniería de Sistemas, UFPSO

## Ejercicio 1: Orientación de tres puntos
Fórmula: det = (Bx − Ax)(Cy − Ay) − (By − Ay)(Cx − Ax)

| Caso | det | Clasificación |
|---|---|---|
| 1 | 18 | Antihorario |
| 2 | -20 | Horario |
| 3 | 0 | Colineal |
| 4 | -15 | Horario |

Complejidad: T = 8 operaciones por terna → O(1); para n ternas, T(n) = 8n → O(n).

## Ejercicio 2: Intersección de segmentos
(Tabla de o1..o4, gráficas de `docs/` y explicación de por qué es O(1))

| Caso | o1 | o2 | o3 | o4 | ¿Intersecta? |
|---|---|---|---|---|---|
| 1 | +26 | −28 | −35 | +19 | Sí, en (4.89, 3.59) |
| 2 | 0 | 0 | 0 | 0 | No (colineales disjuntos) |
| 3 | 0 | 0 | 0 | 0 | Sí (superposición [3,6]) |

## Cómo ejecutar
    pip install -r requirements.txt
    python src/ejercicio1.py
    python src/ejercicio2.py