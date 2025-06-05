def generisi_dijagonale_matricu(n):
    matrica = []
    for i in range(n):
        red = []
        for j in range(n):
            red.append(' ')
        matrica.append(red)
    for i in range(n):
        matrica[i][i] = '*'  
        matrica[i][n - i - 1] = '*'  
    return matrica

# Primer upotrebe:
n = 9
matrica = generisi_dijagonale_matricu(n)
for i in range(n):
    for j in range(n):
        print(matrica[i][j], end=' ')
    print()
