def je_prost(broj):
    if broj < 2:
        return False
    for i in range(2, int(broj**0.5) + 1):
        if broj % i == 0:
            return True
    return False

def saberi_proste_brojeve(do_broja):
    suma = 0
    for n in range(3, do_broja + 1):
        if je_prost(n):
            suma += n
    return suma


n = 10
rezultat = saberi_proste_brojeve(n)
print(f"Suma prostih brojeva do {n} je {rezultat}")
