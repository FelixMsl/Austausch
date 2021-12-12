# RANDOM IMPORTIEREN
import random

# VARIABLEN
n = 0
x = list(random.sample(range(100), 20))

# GIBT DIE LISTE AUS
print(x)

    # PROZESS GEHT NUR BIS 100
while n < 101:

    # GUCKT OB n IN x IST
    if n in x:
        print(n)
        n = n + 1

    else:
        n = n + 1

# SAGT DASS PROZESS BEENDET IST
else: 
    print("Fertig!")