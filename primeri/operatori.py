# Operator za bool vrednosti
a = True
b = False

print("a and b:", a and b)   # logičko i
print("a or b:", a or b)     # logičko ili
print("not a:", not a)       # logička negacija

# Operator za stringove
s1 = "Petnica"
s2 = "Python"

print("s1 + s2:", s1 + " " + s2)   # konkatenacija stringova
print("s1 * 3:", s1 * 3)           # ponavljanje stringa
print("'ni' in s1:", "ni" in s1)   # provera da li se podstring nalazi u stringu
print("'x' not in s2:", "x" not in s2) # provera da li se podstring ne nalazi u stringu

# Operator za brojeve
x = 10
y = 3

print("x + y:", x + y)     # sabiranje
print("x - y:", x - y)     # oduzimanje
print("x * y:", x * y)     # množenje
print("x / y:", x / y)     # deljenje (uvek float)
print("x // y:", x // y)   # celobrojno deljenje
print("x % y:", x % y)     # ostatak pri deljenju
print("x ** y:", x ** y)   # stepenovanje

# Operator poređenja
print("x == y:", x == y)   # jednako
print("x != y:", x != y)   # nije jednako
print("x > y:", x > y)     # veće
print("x < y:", x < y)     # manje
print("x >= y:", x >= y)   # veće ili jednako
print("x <= y:", x <= y)   # manje ili jednako
print("x ∈ (12, 15]", 12 < x <= 15)  # provera da li je u intervalu