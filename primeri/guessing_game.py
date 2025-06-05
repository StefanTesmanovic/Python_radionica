import random

def igra_pogadjanja():
    print("Dobrodošli u igru pogađanja broja!")

    donja_granica = int(input("Unesi donju granicu: "))
    gornja_granica = int(input("Unesi gornju granicu: "))

    if donja_granica >= gornja_granica:
        print("Neispravan opseg. Donja granica mora biti manja od gornje.")
        return

    tajni_broj = random.randint(donja_granica, gornja_granica)
    pokusaji = 5

    print(f"\nPogodi broj između {donja_granica} i {gornja_granica}. Imaš {pokusaji} pokušaja.\n")

    for i in range(1, pokusaji + 1):
        pokusaj = int(input(f"Pokušaj {i}: "))

        if pokusaj == tajni_broj:
            print("Broj je pogodjen")
            break
        elif pokusaj < tajni_broj:
            print("Tajni broj je veći.")
        else:
            print("Tajni broj je manji.")

        if i == pokusaji:
            print(f"\nNažalost, ostao si bez pokušaja. Traženi broj je bio {tajni_broj}.")


igra_pogadjanja()
