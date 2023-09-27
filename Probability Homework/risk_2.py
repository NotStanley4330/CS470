import matplotlib.pyplot as plt
import random
import numpy as np

def simulate_attacker_win_probability(attacker_armies, num_samples=100000):
    win_count = 0
    
    for x in range(num_samples):
        attacker_army = attacker_armies
        defender_army = 5  
        
        while attacker_army > 1 and defender_army > 0:
            na = min(attacker_army - 1, 3)  # Calculate the attackers dice count
            nd = min(defender_army, 2)     # Calculate the defenders dice counr
            
            attacker_dice = sorted([random.randint(1, 6) for _ in range(na)], reverse=True)
            defender_dice = sorted([random.randint(1, 6) for _ in range(nd)], reverse=True)
            
            #iterate through all the dice and elimate the losing armies
            for a, d in zip(attacker_dice, defender_dice):
                if a > d:
                    defender_army -= 1
                elif a < d:
                    attacker_army -= 1
        
        if defender_army == 0:
            win_count += 1
    
    return win_count / num_samples

# Simulate and plot results for attacker armies
attacker_armies_range = range(2, 21)
win_probabilities = [simulate_attacker_win_probability(n) for n in attacker_armies_range]

# Create the plot
plt.plot(attacker_armies_range, win_probabilities)
plt.xlabel("Number of Attacker Armies")
plt.ylabel("Attacker Win Probability")
plt.title("Probability of Attacker Winning the Territory")
plt.grid(True)

# Specify the x-axis tick locations and labels for whole integers
x_ticks = np.arange(min(attacker_armies_range), max(attacker_armies_range) + 1, 1)
plt.xticks(x_ticks)

plt.show()
