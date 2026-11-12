def intro():
    print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.")
    print("Du ska försöka gissa denna kods siffror på max 12 drag.")
    print("Efter respektive gissning så kommer du att få en respons:")
    print("För varje gissad korrekt siffra på korrekt plats i koden: ✓")
    print("För varje gissad korrekt siffra på fel plats i koden: ▒")
    print("För de siffror som inte finns med i koden ges ingen markering.")
    print("\nExempel: om den slumpade koden är 2315")
    print("och du gissar 3165")
    print("så blir responsen ✓ ▒ ▒")
    print("\nDu får välja mellan två svårighetsnivåer:")
    print("Lättare nivå: Alla siffror är garanterat olika.")
    print("Svårare nivå: Det kan finnas upprepningar av en eller flera siffror.")
    while True:
        nivå = input("\nAnge önskad nivå: lättare (1), svårare (2) -> ")
        if nivå == "1" or nivå == "2":
            return int(nivå)
intro()