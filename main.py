def calculator():
    print("Jednoduchá kalkulačka")
    print("Vyber operaci:")
    print("1 - Sčítání")
    print("2 - Odčítání")
    print("3 - Násobení")
    print("4 - Dělení")

    volba = input("Jak chceš pčítat: ")

    a = float(input("Zadej první číslo: "))
    b = float(input("Zadej druhé číslo: "))

    if volba == "1":
        print(f"Výsledek: {a + b}")
    elif volba == "2":
        print(f"Výsledek: {a - b}")
    elif volba == "3":
        print(f"Výsledek: {a * b}")
    elif volba == "4":
        if b != 0:
            print(f"Výsledek: {a / b}")
        else:
            print("Chyba: nelze dělit nulou!")
    else:
        print("Neplatná volba")

calculator()