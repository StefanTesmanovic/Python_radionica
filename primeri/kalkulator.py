brojevi = input("Unesi brojeve za operaciju")
brojevi = brojevi.split()

znak = input("Unesi znak za operaciju (+, -, *, /): ")

a = float(brojevi[0])
b = float(brojevi[1])

if znak == '+':
    rezultat = a + b
elif znak == '-':
    rezultat = a - b
elif znak == '*':
    rezultat = a * b
elif znak == '/':
    if b == 0:
        print("Deljenje sa nulom nije dozvoljeno.")
        exit()
    rezultat = a / b

print("Rezultat:", rezultat)