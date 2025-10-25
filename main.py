import random
import math
crit_chance = 0.16 # change with whatever the base cc of gun in question is
#for weapons with total cc before enervate >200% added bonus is always be +25% total cc avg
enervate = 0.10
j = 0 # enervate cc counter
k = 0 # enervate 'big crit' counter
z = 0 # count amount of base / orange / red crits
p = 0 # for loop for multishot
ms = 3.3 # modded. always 1 if beam weapon, regardless of modded multi. 
ms_max = math.ceil(ms)
ms_min = math.floor(ms)

for i in range(1000000):
    k_incremented = False
    modded_crit = crit_chance * (1 + 2.4) + enervate*j # 2.4 is sentient surge cc (240%)
    j += 1

    if random.randint(0,100)/100 + ms_min > ms:
        simulated_ms = ms_min
    else:
        simulated_ms = ms_max
    
    for p in range(simulated_ms):
        if modded_crit <= 1:
            simulated_crit = random.randint(0, 100)
            if simulated_crit > modded_crit*100:
                z += 0
            else:
                z += 1
        if modded_crit > 2:
            simulated_crit = random.randint(0, 100)
            if simulated_crit > modded_crit*100-200:
                z += 2
                if not k_incremented:
                    k += 1
                    k_incremented = True
            else:
                z += 3
                if not k_incremented:
                    k += 1
                    k_incremented = True
        if modded_crit > 1:
            simulated_crit = random.randint(0, 100)
            if simulated_crit > modded_crit*100-100:
                z += 1
            else:
                z += 2
                if not k_incremented:
                    k += 1
                    k_incremented = True

    if k == 6:
        j = 0
        k = 0
    
print(f"{z/1000000/ms}")
