"""
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza,
ha a paraméterként átvett listaelemek (egész számok) között van páros,
ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!

"""

szamok_listaja = [2, 8, 5, 9, 24]

def paros_e(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
        else:
            return False
megoldas = paros_e(szamok_listaja)
print(f"A számok között van páros: {megoldas}")

szamok_listaja2 = [1, 3, 5, 9, 21]

def paros_e(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
        else:
            return False
megoldas2 = paros_e(szamok_listaja2)
print(f"A számok között van páros: {megoldas2}")