import intro #importerar introduktionsfilen (intro.py)
import mastermind #importerar spelfilen (mastermind.py)

poäng = 0 #antal vinster
antal_omgångar = 0 #antal spelade omgångar
igen = True #variabel för att köra spelet igen (eller första gången i det här fallet)

while igen: #när användaren vill spela
    poäng += mastermind.mastermind(intro.intro()) #kör intro för att få veta svårighetsgrad, kör mastermind och addera resultatet till poängen
    antal_omgångar += 1 #totala antal omgångar ökar med 1
    print(f"\nDu har vunnit {poäng} av {antal_omgångar} omgångar. ", end='') #skriver antal vinster och totala antal omgångar
    while True: #säker inmatning
        svar = input("Vill du spela igen? (j/n) ").lower()
        if svar == "j":
            break #lämnar den säkra inmatningen och återgår till spelet
        elif svar == "n":
            igen = False #gör att den yttersta loopen inte kör någon mer gång 
            break
        else:
            continue #frågar igen
        
print("Programmet avslutades normalt.")