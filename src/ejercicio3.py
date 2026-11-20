from geometria import segmentos_intersectan


def num_llamadas(n):
    """Número exacto de llamadas a intersecta: n(n-1)/2."""
    return n * (n - 1) // 2


def tabla_iteraciones(n):
    print(f"\nTabla de iteraciones n = {n}")
    print(f"{'i':>3} | {'j':<12} | {'llamadas':>8} | {'acumulado':>9}")
    acum = 0
    for i in range(n):
        js = list(range(i + 1, n))
        acum += len(js)
        rango = f"{js[0]}..{js[-1]}" if js else "-"
        print(f"{i:>3} | {rango:<12} | {len(js):>8} | {acum:>9}")
    return acum


def pares_que_se_intersectan(tuberias):
    pares, llamadas = [], 0
    n = len(tuberias)
    for i in range(n):
        for j in range(i + 1, n):          # i+1: sin repetidos ni (i,i)
            llamadas += 1
            a, b = tuberias[i]
            c, d = tuberias[j]
            ok, _ = segmentos_intersectan(a, b, c, d)
            if ok:
                pares.append((i, j))
    return pares, llamadas


if __name__ == "__main__":
    for n in (5, 8):
        assert tabla_iteraciones(n) == num_llamadas(n)

    print("\nComprobaciones esperadas:")
    for n in (100, 1000, 10000):
        print(f"n = {n:>6}: {num_llamadas(n):,}")

    tuberias = [((0, 0), (4, 4)), ((0, 4), (4, 0)), ((5, 5), (6, 6)), ((2, 2), (3, 3))]
    pares, llamadas = pares_que_se_intersectan(tuberias)
    print("\nPares que se intersectan:", pares, "| llamadas:", llamadas)