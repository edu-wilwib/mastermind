import random as rand

def vinst(k):
    if k+1 <= 2:
        print(f"\n\nGrattis! Du vann spelet på {k+1}:a försöket.")
    else:
        print(f"\n\nGrattis! Du vann spelet på {k+1}:e försöket.")
    return 1

def förlust(svar):
    print(f"\n\nNästa gång går det bättre! Rätt rad var: {svar}")
    return 0

def generera_svar(svårighet):
    while True:
        svar = ""
        for i in range(4):
            svar += str(rand.randint(1, 6))
        if svårighet == 1:
            if len(set(svar)) < 4:
                continue
        return svar

def feedback(gissning, svar):
    rätt = 0
    fel = 0
    svar_lista = list(svar)
    gissning_lista = list(gissning)
    for j in range(4):
        if gissning[j] == svar[j]:
            rätt += 1
            svar_lista[j] = None
            gissning_lista[j] = None
    for l in gissning_lista:
        if not l == None:
            n = 0
            for m in svar_lista:
                if l == m:
                    fel += 1
                    svar_lista[n] = None
                    break
                n +=1
    return f"{rätt*'☑ '}{fel*'☐ '}"

def mastermind(svårighet):
    svar = generera_svar(svårighet)
    
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
            feedback_historia[k] = feedback(gissning, svar)
            if not gissning_historia[11-i] == "    ":
                sträng += feedback_historia[11-i]
        print(sträng, end='')
        if gissning == svar:
            return vinst(k)
    return förlust(svar)