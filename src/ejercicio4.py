import os
import matplotlib.pyplot as plt
from geometria import orientacion

terreno = {"A": (0, 0), "B": (8, 0), "C": (8, 6), "D": (4, 3), "E": (0, 6)}


def area_con_signo(poly):
    s = 0
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % len(poly)]
        s += x1 * y2 - x2 * y1
    return s / 2


def clasificar_vertices(poly):
    """Asume polígono CCW."""
    n = len(poly)
    res = []
    for i in range(n):
        det = orientacion(poly[i - 1], poly[i], poly[(i + 1) % n])
        res.append((i, det, "convexo" if det > 0 else "cóncavo" if det < 0 else "colineal"))
    return res


def conteo_triangulacion(n):
    """Triángulos (n-2) y diagonales internas (n-3)."""
    if n < 3:
        raise ValueError("Un polígono necesita al menos 3 vértices")
    return n - 2, n - 3


def punto_en_triangulo(p, a, b, c):
    """Incluye el borde (criterio conservador). Triángulo CCW."""
    return (orientacion(a, b, p) >= 0 and
            orientacion(b, c, p) >= 0 and
            orientacion(c, a, p) >= 0)


def ear_clipping(poly):
    idx = list(range(len(poly)))
    triangulos, diagonales = [], []
    while len(idx) > 3:
        for k in range(len(idx)):
            ip, ic, inx = idx[k - 1], idx[k], idx[(k + 1) % len(idx)]
            a, b, c = poly[ip], poly[ic], poly[inx]
            if orientacion(a, b, c) <= 0:
                continue
            if any(punto_en_triangulo(poly[j], a, b, c)
                   for j in idx if j not in (ip, ic, inx)):
                continue
            triangulos.append((ip, ic, inx))
            diagonales.append((ip, inx))
            idx.pop(k)
            break
        else:
            raise ValueError("Polígono no simple o no está en sentido CCW")
    triangulos.append(tuple(idx))
    return triangulos, diagonales


def graficar(poly, nombres, triangulos, ruta="docs/triangulacion.png"):
    fig, ax = plt.subplots(figsize=(6, 5))
    xs = [p[0] for p in poly] + [poly[0][0]]
    ys = [p[1] for p in poly] + [poly[0][1]]
    ax.plot(xs, ys, "k-", linewidth=2)
    for t in triangulos:
        pts = [poly[i] for i in t] + [poly[t[0]]]
        ax.plot([p[0] for p in pts], [p[1] for p in pts], "r--")
    for nombre, p in zip(nombres, poly):
        ax.annotate(nombre, p, textcoords="offset points", xytext=(6, 6), fontsize=12)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title("Triangulación por ear clipping")
    os.makedirs("docs", exist_ok=True)
    fig.savefig(ruta, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    nombres = list(terreno.keys())
    poly = list(terreno.values())
    print("Área con signo:", area_con_signo(poly), "(positiva = CCW)")

    print("\n1. Vértices:")
    for i, det, tipo in clasificar_vertices(poly):
        print(f"   {nombres[i]}: det = {det:>4} -> {tipo}")

    t, d = conteo_triangulacion(len(poly))
    print(f"\n2. n = {len(poly)} -> {t} triángulos, {d} diagonales internas")

    tris, diags = ear_clipping(poly)
    print("\n3/4. Ear clipping (en orden de recorte):")
    for tri, dg in zip(tris, diags):
        print("   oreja/triángulo:", [nombres[i] for i in tri],
              "| diagonal:", nombres[dg[0]] + "-" + nombres[dg[1]])
    print("   triángulo final:", [nombres[i] for i in tris[-1]])
    graficar(poly, nombres, tris)

    print("\nTabla n -> (triángulos, diagonales):")
    for n in (3, 4, 5, 10, 100):
        print(f"   n = {n:>3}: {conteo_triangulacion(n)}")