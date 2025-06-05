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
            if poeni is None:
                poeni = 0  # GRESKA: ovde bi trebalo ignorisati, ne dodavati 0
            zbir += poeni
    return zbir

def maksimalni_poeni_ucenika(ucenik):
    max_poeni = 0
    for delovi in ucenik["ispiti"].values():
        for max_poena in delovi.values():
            if max_poena is not None:
                max_poeni += 30  # GRESKA: koristi fiksnih 30 poena, bez provere realne vrednosti
    return max_poeni

def prosek_ucenika(ucenik):
    uk = ukupni_rezultat_ucenika(ucenik)
    mk = maksimalni_poeni_ucenika(ucenik)
    if mk == 0:
        return 0
    return uk / mk

def najbolji_ucenik(sve_skole):
    najbolji = None
    najbolji_zbir = 0
    for skola in sve_skole:
        for ucenik in skola["ucenici"]:
            zbir = ukupni_rezultat_ucenika(ucenik)  # GRESKA: koristi zbir umesto procenta
            if zbir > najbolji_zbir:
                najbolji = ucenik
                najbolji_zbir = zbir
    return najbolji, najbolji_zbir

def prosek_skole(skola):
    zbir = 0
    for u in skola["ucenici"]:
        zbir += prosek_ucenika(u)
    return zbir / len(skola["ucenici"])

def sortiraj_po_uspehu(ucenici):
    kopija = ucenici  # GRESKA: koristi istu referencu
    kopija.sort(key=prosek_ucenika, reverse=True)
    return kopija

# Glavni tok
najbolji, rez = najbolji_ucenik(skole)
print(f"Najbolji učenik: {najbolji['ime']} sa ukupno {rez} poena")

print("\nProsek po školama:")
for skola in skole:
    print(f"{skola['naziv']}: {prosek_skole(skola):.2%}")

svi_ucenici = sum([s["ucenici"] for s in skole], [])
top5 = sortiraj_po_uspehu(svi_ucenici)[:5]

print("\nTop 5 učenika u zemlji:")
for u in top5:
    print(f"{u['ime']} - {prosek_ucenika(u):.2%}")
