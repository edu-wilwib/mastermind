import random as rand

def vinst(k): #funktion för vinst definieras där k är antalet gissningar minus 1
    if k+1 <= 2: #skriver 1:a eller 2:a
        print(f"\n\nGrattis! Du vann spelet på {k+1}:a försöket.")
    else: #skriver 3:e, 4:e etc.
        print(f"\n\nGrattis! Du vann spelet på {k+1}:e försöket.")
    return 1 #funktionen returnerar värdet 1

def förlust(svar): #funktionen för förlust definieras
    print(f"\n\nNästa gång går det bättre! Rätt rad var: {svar}") #skriver svaret
    return 0 #funktionen returnerar värdet 0

def generera_svar(svårighet): #funktion för att generara ett svar definieras
    while True:
        svar = ""
        for i in range(4): #slumpar fram ett fyrsiffrigt svar med siffrorna 1-6
            svar += str(rand.randint(1, 6)) #lägger in siffra i sträng
        if svårighet == 1: #om svårigheten är 1 (lätt svårighet, inga siffror får upprepas i svaret)
            if len(set(svar)) < 4: #gör om strängen svar till set (oordnad lista utan dubletter) och kollar om något har försvunnit
                continue #genererar ett nytt svar
        return svar #funktionen returnerar det genererade svaret

def feedback(gissning, svar): #funktionen för feedback definieras
    rätt = 0 #antal rätt på rätt plats
    fel = 0 #antal rätt på fel plats
    svar_lista = list(svar) #skapar en lista av svaret (som får ändras)
    gissning_lista = list(gissning) #skapar en lista av gissningen (som får ändras)
    for j in range(4): #kollar hur många rätt på rätt plats
        if gissning[j] == svar[j]: #när en siffra är samma i svaret och gissningen
            rätt += 1 #rätt på rätt plats adderas med 1
            svar_lista[j] = None #tar bort siffran från svarslistan
            gissning_lista[j] = None #tar bort siffran från gissningslistan
    for l in gissning_lista: #kollar hur många rätt på fel plats
        if not l == None: #om det finns en siffra (om siffran inte var rätt på rätt plats)
            n = 0 #räknevariabel
            for m in svar_lista: #går igenom varje index i svarslistan för varje siffra i gissningslistan (som inte blev borttagna)
                if l == m: #kollar om det är samma siffra
                    fel += 1 #rätt på fel plats adderas med 1
                    svar_lista[n] = None #tar bort siffran från svarslistan (så att den inte räknar samma siffra flera gången)
                    break #lämnar loopen så att den inte tar bort alla index med samma siffra
                n += 1
    return f"{rätt*'☑ '}{fel*'☐ '}" #funktionen returnerar en sträng med feedback

def mastermind(svårighet): #funktionen för mastermindspel definieras
    svar = generera_svar(svårighet) #generarar ett svar (med funktionen generera_svar)
    
    feedback_historia = [] #skapar en lista som ska användas till all tidigare feedback
    gissning_historia = [] #skapar en lista som ska användas till alla tidigare gissningar
    for i in range(12): #för varje av de 12 framtida gissningarna
        gissning_historia.append("    ") #fyller gissning_historia med 12 index
        feedback_historia.append("    ") #fyller feedback_historia med 12 index
    
    for k in range(12): #spelloop
        print("\n")
        while True: #säker inmatning på gissning
            gissning = input("Ange en gissning som följd av 4 siffror -> ")
            if len(gissning) != 4: #om gissningens längd inte är 4
                continue #ny gissning
            elif gissning in gissning_historia: #om man försöker gissa på samma sak igen
                continue #ny gissning
            try:
                int(gissning) #kollar att gissningen är ett heltal
            except ValueError: #om det inte är det
                continue #ny gissning
            gissning_historia[k] = gissning #lägger till gissning på rätt plats i gissning_historia
            break
        sträng = f"Drag #{4*' '}Drag{7*' '}Feedback\n{38*'-'}" #skapar en sträng att skriva ut, börjar med rubrik
        for i in range(12): #för varje av de 12 (vissa framtida) gissningarna
            sträng += f"\n\n{(12-i):>2}{6*' '}{gissning_historia[11-i]}{7*' '}" #skriver en rad i strängen (formas som en tabell, feedbacken kommer senare)
            feedback_historia[k] = feedback(gissning, svar) #beräknar feedback på alla gissningar i gissning_historia
            if not gissning_historia[11-i] == "    ": #om det finns en gissning på det indexet
                sträng += feedback_historia[11-i] #lägg till feedbacken i strängen (längst bak i raden)
        print(sträng, end='') #skriver ut strängen
        if gissning == svar: #om man gissade rätt
            return vinst(k) #kör funktionen vinst, och returnerar värdet man får
    return förlust(svar) #om gissningarna tar slut, kör funktionen förlust, och returnerar värdet man får