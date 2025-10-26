import random
import math

modded_crit = 0.16 * (1 + 2.4) + 0.25 # crit before enervate is counted
# for weapons with total cc before enervate >200% added bonus is always be +25% total cc avg
enervate = 0.10
j = 0 # enervate cc counter
k = 0 # enervate 'big crit' counter
z = 0 # count amount of base / yellow / orange / red crits (0 / 1 / 2 / 3)
p = 0 # for loop for multishot
ms = 1 # modded. always 1 if beam weapon, regardless of modded multi. 
ms_max = math.ceil(ms)
ms_min = math.floor(ms)

for i in range(1000000):
    k_incremented = False
    total_crit = modded_crit + enervate * j 
    j += 1

    if random.randint(0,100)/100 + ms_min > ms:
        simulated_ms = ms_min
    else:
        simulated_ms = ms_max
    
    for p in range(simulated_ms):
        if total_crit <= 1:
            simulated_crit = random.randint(0, 1000)
            if simulated_crit > total_crit*1000:
                z += 0
            else:
                z += 1
        if total_crit >= 2:
            simulated_crit = random.randint(0, 1000)
            if simulated_crit > total_crit*1000-2000:
                z += 2
                if not k_incremented:
                    k += 1
                    k_incremented = True
            else:
                z += 3
                if not k_incremented:
                    k += 1
                    k_incremented = True
        if 2 > total_crit > 1:
            simulated_crit = random.randint(0, 1000)
            if simulated_crit > total_crit*1000-1000:
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
