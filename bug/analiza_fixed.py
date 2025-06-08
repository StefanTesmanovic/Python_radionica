from skole_podaci import skole_podaci, predmeti_podaci
from copy import deepcopy

skole = skole_podaci

def maksimalni_poeni_ucenika(ucenik):
    max = 0
    for predmet in ucenik.keys():
        for deo in ucenik[predmet].keys():
            poeni = ucenik[predmet][deo]
            if poeni is not None:
                max += predmeti_podaci[predmet][deo] # ovde sam cackao
    return max

def ukupni_rezultat_ucenika(ucenik):
    ukupno = 0
    for predmet in ucenik.keys():
        for deo in ucenik[predmet].keys():
            poeni = ucenik[predmet][deo]
            if poeni is not None:                   # ovde sam cackao
                ukupno += poeni
    return ukupno

def prosek_ucenika(ucenik):
    uk = ukupni_rezultat_ucenika(ucenik)
    mk = maksimalni_poeni_ucenika(ucenik)
    if mk == 0:
        return 0
    return uk / mk

def najbolji_ucenik(skole):
    najbolji = None
    najbolji_procenat = 0                   # ovde sam cackao
    for skola in skole.keys():
        for ucenik in skole[skola].keys():
            procenat = prosek_ucenika(skole[skola][ucenik])
            if procenat > najbolji_procenat: # ovde sam cackao
                najbolji = ucenik
                najbolji_procenat = procenat
    return najbolji, najbolji_procenat

def prosek_skole(skola):
    zbir = 0
    for ucenik in skola.keys():
        zbir += prosek_ucenika(skola[ucenik])
    return zbir / len(skola)

def sortiraj_po_uspehu(ucenici):
    kopija = deepcopy(ucenici)
    kopija = [(k, prosek_ucenika(v)) for k, v in kopija.items()] 
    # pravi listu uredjenih parova (ime, procenat), for k,v in kopija.items()
    #  može da se stavi jer kopija.items() bude uređeni par i onda k bude prvi element uređenog para, a v drugi element uređenog para
    #  Ti elementi u uređenom paru su ključ i vrednost
    kopija = sorted(kopija, key=lambda x: x[1], reverse=True)
    return kopija



najbolji, rez = najbolji_ucenik(skole)
print(f"Najbolji učenik: {najbolji} sa uspešnošću {rez:.2%}")

print("\nProsek po školama:")
for skola in skole.keys():
    print(f"{skola}: {prosek_skole(skole[skola]):.2%}")


svi_ucenici = {}
for skola in skole.keys():
    svi_ucenici |= skole[skola]

top5 = sortiraj_po_uspehu(svi_ucenici)[:5]

print("\nTop 5 učenika u zemlji:")
for ime, procenat in top5:
    print(f"{ime} - {procenat:.2%}")
