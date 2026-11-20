import os
import matplotlib.pyplot as plt
from geometria import orientacion, segmentos_intersectan

casos = {
    1: ((1, 1), (7, 5), (2, 6), (8, 1)),
    2: ((1, 1), (3, 3), (5, 5), (7, 7)),
    3: ((0, 2), (6, 2), (3, 2), (9, 2)),
}

def graficar(n, a, b, c, d, resultado):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot([a[0], b[0]], [a[1], b[1]], "o-", color="blue", label="AB")
    ax.plot([c[0], d[0]], [c[1], d[1]], "o-", color="red", label="CD")
    for nombre, p in zip("ABCD", (a, b, c, d)):
        ax.annotate(nombre, p, textcoords="offset points", xytext=(5, 5))
    ax.set_title(f"Caso {n}: {resultado}")
    ax.grid(True)
    ax.legend()
    ax.set_aspect("equal")
    os.makedirs("docs", exist_ok=True)
    fig.savefig(f"docs/caso{n}.png", dpi=150)
    plt.close(fig)

if __name__ == "__main__":
    for n, (a, b, c, d) in casos.items():
        o = (orientacion(a, b, c), orientacion(a, b, d),
             orientacion(c, d, a), orientacion(c, d, b))
        ok, tipo = segmentos_intersectan(a, b, c, d)
        print(f"Caso {n}: o1..o4 = {o} -> {'SÍ' if ok else 'NO'} ({tipo})")
        graficar(n, a, b, c, d, tipo)