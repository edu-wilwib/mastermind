import random as rand

def mastermind(svårighet):
    while True:
        svar = ""
        for i in range(4):
            svar += str(rand.randint(1, 6))
        if svårighet == 1:
            if len(set(svar)) < 4:
                continue
        break
    
    feedback_historia = []
    gissning_historia = []
    for i in range(12):
        gissning_historia.append("    ")
        feedback_historia.append("    ")
    
    
    for k in range(12):
        print("\n")
        while True:
            gissning = input("Ange en gissning som följd av 4 siffror -> ")
            if len(gissning) != 4:
                continue
            elif gissning in gissning_historia:
                continue
            try:
                int(gissning)
            except ValueError:
                continue
            gissning_historia[k] = gissning
            break
        sträng = f"Drag #{4*' '}Drag{7*' '}Feedback\n{38*'-'}"
        for i in range(12):
            sträng += f"\n\n{(12-i):>2}{6*' '}{gissning_historia[11-i]}{7*' '}"
            rätt = 0
            fel = 0
            for j in range(4):
                if gissning[j] == svar[j]:
                    rätt += 1
                elif gissning[j] in svar:
                    fel += 1
            feedback_historia[i] = f"{rätt*'✓ '}{fel*'▒ '}"
            if not gissning_historia[11-i] == "    ":
                sträng += feedback_historia[i]
        print(sträng, end='')
mastermind(2)