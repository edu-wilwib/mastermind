import intro
import mastermind

while True:
    mastermind(intro.intro())
    if not input("Vill du spela igen? (j/n) ") == "j":
        break