import mastermind

def intro():
    print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.")
    print("Du ska försöka gissa denna kods siffror på max 12 drag.")
    print("Efter respektive gissning så kommer du att få en respons:")
    print("För varje gissad korrekt siffra på korrekt plats i koden: ✓")
    print("För varje gissad korrekt siffra på fel plats i koden: ▒")
    print("För de siffror som inte finns med i koden ges ingen markering.")
    svar = mastermind.generera_svar(1)
    print(f"\nExempel: om den slumpade koden är {svar}")
    gissning = mastermind.generera_svar(1)
    print(f"och du gissar {gissning}")
    print(f"så blir responsen {mastermind.feedback(gissning, svar)}")
    print("\nDu kan skriva 0 i din gissning för att testa en idé utan att 0:an kan vara rätt.")
    print("\nDu får välja mellan två svårighetsnivåer:")
    print("Lättare nivå: Alla siffror är garanterat olika.")
    print("Svårare nivå: Det kan finnas upprepningar av en eller flera siffror.")
    while True:
        nivå = input("\nAnge önskad nivå: lättare (1), svårare (2) -> ")
        if nivå == "1" or nivå == "2":
            return int(nivå)