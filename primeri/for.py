n = int(input("Unesi broj elemenata liste: "))
lista = []
for i in range(n):          # pokazi druge mogucnosti sa for petljom, koraci i tako to
    lista.append(i)

for element in lista:       # ili in range(len(lista)):
    print(f"Element: {element}, Element^2: {element**2}")

