"""
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja,
hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!

"""


szamok_listaja = [2, 3, 23, 27, 36, 9]
def harommal_oszthatok(numbers):
    darab = 0
    for num in numbers:
        if num % 3 == 0:
            darab += 1
    return darab
megoldas = harommal_oszthatok(szamok_listaja)
print(f"Ennyi 3-mal osztható szám van benne: {megoldas}")
