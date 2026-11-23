import intro
import mastermind

poäng = 0
antal_omgångar = 0
igen = True

while True:
    if igen:
        poäng += mastermind.mastermind(intro.intro())
        antal_omgångar += 1
        print(f"\nDu har vunnit {poäng} av {antal_omgångar} omgångar. ", end='')
        while True:
            svar = input("Vill du spela igen? (j/n) ").lower()
            if svar == "j":
                break
            elif svar == "n":
                igen = False
                break
            else:
                continue
    else:
        break
print("Programmet avslutades normalt.")