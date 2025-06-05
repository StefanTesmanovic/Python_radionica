a = 42
b = 3.14
c = "Zdravo, svet!"
d = True
e = [1, 2, 3, 4, 5]
f = (1, 2, 3)
g = {"ime": "Ana", "godine": 25}
g["mesto"] = "petnica"
g["godine"] += 1
h = {1, 2, 3}
i = None


tipovi = [a, b, c, d, e, f, g, h, i]
for x in tipovi:
    print(f"Vrednost: {x}, Tip: {type(x)}")
