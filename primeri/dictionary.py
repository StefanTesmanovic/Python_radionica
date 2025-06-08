# Osnovne operacije sa rečnicima
student = {
    "ime": "Ana",
    "godine": 20,
    "fakultet": "ETF"
}

print("Ime:", student["ime"])
print("Godine:", student["godine"])
print("Fakultet:", student["fakultet"])

student["grad"] = "Beograd"
print("Posle dodavanja grada:", student)

student["godine"] = 21
print("Posle izmene godina:", student)

# Brisanje para ključ-vrednost
del student["fakultet"]
print("Posle brisanja fakulteta:", student)

# Svi ključevi
print("Ključevi:", student.keys())
# Sve vrednosti 
print("Vrednosti:", student.values())

for kljuc, vrednost in student.items():
    print(f"{kljuc}: {vrednost}")

# Ugnježdeni rečnici
studenti = {
    "student1": {
        "ime": "Ana",
        "godine": 20
    },
    "student2": {
        "ime": "Marko",
        "godine": 22
    }
}

print("Ugnježdeni rečnici:")
for kljuc, vrednost in studenti.items():
    print(f"{kljuc}: {vrednost['ime']}, {vrednost['godine']} godina")