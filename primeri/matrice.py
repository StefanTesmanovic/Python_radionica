dimenzije = input("Unesite dimenzije matrice (redovi, kolone): ")
redovi, kolone = map(int, dimenzije.split(' '))

matrica = []
for i in range(redovi):
    red = []
    for j in range(kolone):
        element = int(input(f"Unesite element [{i}][{j}]: "))
        red.append(element)
    matrica.append(red)

for i in range(redovi):
    for j in range(kolone):
        print(matrica[i][j], end=' ')
    print()
