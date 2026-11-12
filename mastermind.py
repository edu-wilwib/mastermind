import random as rand

def mastermind(svårighet):
    while True:
        svar = rand.randint(0, 6666)
        if "7" in str(svar) or "8" in str(svar) or "9" in str(svar):
            continue
        if svårighet == 1:
            if len(set(str(svar))) < 4:
                continue
        svar = str(svar)
        break
    
    for i in range(12):
        print("\n")
        while True:
            gissning = input("Ange en gissning som följd av 4 siffror -> ")
            if len(gissning) != 4:
                continue
            try:
                int(gissning)
            except ValueError:
                continue
            break
            