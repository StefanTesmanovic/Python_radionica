def crtaj_vetrenjacu(n=15):
    if n % 2 == 0:
        print("Dimenzija mora biti neparna!")
        return
    vet = []
    centar = n // 2
    for i in range(n):
        red = []
        for j in range(n):
            if i == j or i + j == n - 1 or i == centar or j == centar:
                red.append("*")
            elif i < centar and j < centar and j > i:
                red.append("*")
            elif i < centar and j > centar and j > n - 1 - i:
                red.append("*")
            elif i > centar and j > centar and j < i:
                red.append("*")
            elif i > centar and j < centar and j < n - 1 - i:
                red.append("*")
            else:
                red.append(" ")
        vet.append(red)
    for i in range(n):
        for j in range(n):
            print(vet[i][j], end=' ')
        print()

crtaj_vetrenjacu(15)
