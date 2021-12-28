import random
import sys
import time
from suspense import suspenseprint

lives = 5
secret = random.randrange(1,11)

suspenseprint("to pensando num numero de 1 ate 10.")

while lives > 0:
    suspenseprint("adivinha!")
    print("tu tens", lives, "tentativas.")
    guess = input()
    guess = int(guess)
    lives = lives - 1
    if guess == secret:
        suspenseprint("Parabens!")
        sys.exit(0)
    elif lives > 0:
        if guess < secret:
            suspenseprint("meu numero eh maior")
        else:
            suspenseprint("meu numero eh menor")

print("fuen fuen fuen, meu numero era o ", secret)

