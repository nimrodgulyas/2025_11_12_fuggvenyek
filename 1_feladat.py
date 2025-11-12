"""
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, 
ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!
"""
szamok = [5, 2, 31, 25, 56, 78]
def osszegzo(szamok):
    sum_numbers = 0
    for num in szamok:
        sum_numbers = sum_numbers + num
    return sum_numbers
szamok_osszege = osszegzo(szamok)
print(f"A számok összege: {szamok_osszege}")