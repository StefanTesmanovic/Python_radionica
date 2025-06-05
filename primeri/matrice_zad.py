n = int(input("Unesite broj vrsta matrice: "))
m = int(input("Unesite broj kolona matrice: "))
matrica = []
for i in range(n):
    red = list(map(int, input().split()))
    matrica.append(red)

for i in range(n):
    zbir = 0
    for j in range(m):
        zbir += matrica[i][j]
    print(f"Zbir elemenata u {i+1}. vrsti je {zbir}")