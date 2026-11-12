import intro
import mastermind

while True:
    mastermind.mastermind(intro.intro())
    if not input("Vill du spela igen? (j/n) ").lower() == "j":
        break