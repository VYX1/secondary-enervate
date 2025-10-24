import random
crit_chance = 0.16 # change with whatever the base cc of gun in question is
enervate = 0.10
j = 0
k = 0
z = 0

for i in range(100000):
    
    modded_crit = crit_chance * (1 + 2.4 + enervate*j) #2.4 is sentient surge cc
    j += 1

    if modded_crit <= 1:
        simulated_crit = random.randint(0, 100)
        if simulated_crit > modded_crit*100:
            z += 0
        else:
            z += 1
    if modded_crit > 1:
        simulated_crit = random.randint(0, 100)
        if simulated_crit > modded_crit*100-100:
            z += 1
        else:
            z += 2
            k += 1

    if k == 6:
        j = 0
        k = 0
    
print(f"{z/100000}")