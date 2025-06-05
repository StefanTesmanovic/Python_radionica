import random
import json

def generisi_ispite():
    return {
        "matematika": {"teorija": random.randint(0, 30), "prakticno": random.randint(0, 30)},
        "fizika": {"teorija": random.randint(0, 20), "prakticno": None if random.random() < 0.1 else random.randint(0, 20)},
        "hemija": {"test": random.randint(0, 25), "laboratorija": random.randint(0, 25)},
        "programiranje": {"algoritmi": random.randint(0, 40), "projektni_rad": random.randint(0, 30)},
        "srpski": {"esej": random.randint(0, 20), "gramatika": random.randint(0, 20)}
    }

def generisi_ucenika(ime):
    return {
        "ime": ime,
        "ispiti": generisi_ispite()
    }

def generisi_skole():
    return [
        {
            "naziv": "Gimnazija",
            "ucenici": [generisi_ucenika(ime) for ime in ["Ana", "Marko", "Luka", "Teodora"]]
        },
        {
            "naziv": "Prva Tehnička",
            "ucenici": [generisi_ucenika(ime) for ime in ["Ivana", "Stefan", "Milica", "Nikola"]]
        },
        {
            "naziv": "Računarska škola",
            "ucenici": [generisi_ucenika(ime) for ime in ["Nemanja", "Jelena", "Filip", "Tamara"]]
        }
    ]

if __name__ == "__main__":
    podaci = generisi_skole()
    with open("skole_podaci.json", "w", encoding="utf-8") as f:
        json.dump(podaci, f, ensure_ascii=False, indent=4)
