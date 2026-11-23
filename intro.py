import mastermind #importerar filen mastermind.py (för att få funktionerna för att generara och få feedback på svar)

def intro(): #en funktion för att skriva introduktionen och fråga vilken svårighetsgrad man vill ha på spelet
    print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.")
    print("Du ska försöka gissa denna kods siffror på max 12 drag.")
    print("Efter respektive gissning så kommer du att få en respons:")
    print("För varje gissad korrekt siffra på korrekt plats i koden: ✓")
    print("För varje gissad korrekt siffra på fel plats i koden: ▒")
    print("För de siffror som inte finns med i koden ges ingen markering.")
    svar = mastermind.generera_svar(1) #genererar ett svar
    print(f"\nExempel: om den slumpade koden är {svar}")
    gissning = mastermind.generera_svar(1) #generarar en gissning som skulle kunna vara rätt
    print(f"och du gissar {gissning}")
    print(f"så blir responsen {mastermind.feedback(gissning, svar)}") #skriver feedbacken på svaret kontra gissningen
    print("\nDu kan skriva 0 i din gissning för att testa en idé utan att 0:an kan vara rätt.")
    print("\nDu får välja mellan två svårighetsnivåer:")
    print("Lättare nivå: Alla siffror är garanterat olika.")
    print("Svårare nivå: Det kan finnas upprepningar av en eller flera siffror.")
    while True: #säker inmatning
        nivå = input("\nAnge önskad nivå: lättare (1), svårare (2) -> ")
        if nivå == "1" or nivå == "2":
            return int(nivå) #funktionen returnerar angiven nivå