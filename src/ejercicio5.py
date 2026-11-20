def Ta(n):
    """Modelo cuadrático: ear clipping con listas de convexos/cóncavos."""
    return n ** 2


def Tb(n):
    """Modelo cúbico: probar todas las diagonales (n^2) contra n aristas."""
    return n ** 3


if __name__ == "__main__":
    print(f"{'n':>7} | {'Ta = n^2':>14} | {'Tb = n^3':>20} | {'Tb/Ta':>7}")
    for n in (5, 8, 10, 100, 1000, 10000):
        print(f"{n:>7} | {Ta(n):>14,} | {Tb(n):>20,} | {Tb(n) // Ta(n):>7}")