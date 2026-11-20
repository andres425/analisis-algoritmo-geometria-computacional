def orientacion(a, b, c):
    """Determinante de orientación de tres puntos.
    > 0 antihorario, < 0 horario, = 0 colineal."""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def clasificar(det):
    if det > 0:
        return "Giro antihorario"
    if det < 0:
        return "Giro horario"
    return "Colineal"


def en_rango(a, b, p):
    """Verifica si p (colineal con a-b) está dentro del bounding box de a-b."""
    return (min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and
            min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))


def segmentos_intersectan(a, b, c, d):
    """Devuelve (bool, tipo) para los segmentos AB y CD. Complejidad O(1)."""
    o1 = orientacion(a, b, c)
    o2 = orientacion(a, b, d)
    o3 = orientacion(c, d, a)
    o4 = orientacion(c, d, b)

    # Intersección propia
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True, "Propia (cruce)"

    # Casos especiales: contacto o superposición
    if o1 == 0 and en_rango(a, b, c):
        return True, "Contacto/superposición"
    if o2 == 0 and en_rango(a, b, d):
        return True, "Contacto/superposición"
    if o3 == 0 and en_rango(c, d, a):
        return True, "Contacto/superposición"
    if o4 == 0 and en_rango(c, d, b):
        return True, "Contacto/superposición"

    return False, "Sin intersección"