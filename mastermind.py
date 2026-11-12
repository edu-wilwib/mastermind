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
    
    gissning_historia = []
    
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
            gissning_historia.append(gissning)
            break
        sträng = f"Drag #{4*' '}Drag{7*' '}Feedback\n{38*'-'}"
        print(sträng)
mastermind(2)