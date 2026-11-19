import intro
import mastermind

poäng = 0
antal_omgångar = 0

while True:
    poäng += mastermind.mastermind(intro.intro())
    antal_omgångar += 1
    print(f"\nDu har vunnit {poäng} av {antal_omgångar} omgångar. ", end='')
    if not input("Vill du spela igen? (j/n) ").lower() == "j":
        break