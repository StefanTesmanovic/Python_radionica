n = int(input("Unesite broj n: "))

zbir = 0
for i in range(1, n + 1):
    zbir += i

print("Zbir prvih", n, "brojeva je:", zbir)