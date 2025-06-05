import json
from copy import deepcopy

def ucitaj_podatke(putanja="skole_podaci.json"):
    with open(putanja, "r", encoding="utf-8") as f:
        return json.load(f)

skole = ucitaj_podatke()

def ukupni_rezultat_ucenika(ucenik):
    zbir = 0
    for predmet, delovi in ucenik["ispiti"].items():
        for deo, poeni in delovi.items():
            if poeni is not None:
                zbir += poeni  # ✅ Ispravljeno: ignorišemo None vrednosti
    return zbir

def maksimalni_poeni_ucenika(ucenik):
    max_poeni = 0
    for delovi in ucenik["ispiti"].values():
        for poeni in delovi.values():
            if poeni is not None:
                max_poeni += poeni  # ✅ Ispravljeno: koristimo stvarne maksimalne poene, ne fiksnih 30
    return max_poeni

def prosek_ucenika(ucenik):
    uk = ukupni_rezultat_ucenika(ucenik)
    mk = maksimalni_poeni_ucenika(ucenik)
    if mk == 0:
        return 0
    return uk / mk

def najbolji_ucenik(sve_skole):
    najbolji = None
    najbolji_procenat = 0
    for skola in sve_skole:
        for ucenik in skola["ucenici"]:
            procenat = prosek_ucenika(ucenik)  # ✅ Ispravljeno: koristi se procenat uspeha, ne zbir
            if procenat > najbolji_procenat:
                najbolji = ucenik
                najbolji_procenat = procenat
    return najbolji, najbolji_procenat

def prosek_skole(skola):
    zbir = 0
    for u in skola["ucenici"]:
        zbir += prosek_ucenika(u)
    return zbir / len(skola["ucenici"])

def sortiraj_po_uspehu(ucenici):
    kopija = deepcopy(ucenici)  # ✅ Ispravljeno: koristi deepcopy da ne menja original
    kopija.sort(key=prosek_ucenika, reverse=True)
    return kopija

# Glavni tok
najbolji, rez = najbolji_ucenik(skole)
print(f"Najbolji učenik: {najbolji['ime']} sa uspešnošću {rez:.2%}")

print("\nProsek po školama:")
for skola in skole:
    print(f"{skola['naziv']}: {prosek_skole(skola):.2%}")

svi_ucenici = sum([s["ucenici"] for s in skole], [])
top5 = sortiraj_po_uspehu(svi_ucenici)[:5]

print("\nTop 5 učenika u zemlji:")
for u in top5:
    print(f"{u['ime']} - {prosek_ucenika(u):.2%}")
