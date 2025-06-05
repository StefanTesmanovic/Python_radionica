import nad
list = []

while True:
    element = int(input("Unesite broj (ili -1 za kraj): "))
    if element == -1:
        break
    list.append(element)

for element in list:
    print(f"Element: {element}, Faktorijel: {nad.faktorijel(element)}")