from geometria import orientacion, clasificar

casos = {
    1: ((1, 2), (5, 3), (3, 7)),
    2: ((2, 1), (6, 5), (8, 2)),
    3: ((1, 1), (3, 3), (6, 6)),
    4: ((0, 4), (5, 4), (3, 1)),
}

# T(n): 7 operaciones aritméticas + 1 comparación = 8 por terna -> O(1)
# Para n ternas: T(n) = 8n -> O(n)
if __name__ == "__main__":
    for n, (a, b, c) in casos.items():
        det = orientacion(a, b, c)
        print(f"Caso {n}: A{a} B{b} C{c} -> det = {det:>4} -> {clasificar(det)}")