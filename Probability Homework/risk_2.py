import matplotlib.pyplot as plt
import random


#Assume that the defender starts out with 5 armies in the territory. Your
# task is to estimate, for all numbers of attacker armies between 2 and 20,
# the probability that the attacker will win the territory. The attacker wins
# the territory if all of the defender armies are lost. As the battle progresses,
# the dice rolling will continue, with each player using the maximum number
# of dice allowed given their number of armies, until either the defender has
# lost all of their armies or the attacker only has 1 army remaining. Again,
# the attacker wins the territory if the defender armies are entirely lost.
# Plot out your results showing this attacker-win-probability (y-axis) for
# each different number of attacker armies (x-axis). Make sure your plot
# is labeled appropriately. What is the minimum number of armies the
# attacker needs to guarantee a 50% chance of winning the territory? How
# about to guarantee an 80% chance of winning?

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

plt.plot(attacker_armies_range, win_probabilities)
plt.xlabel("Number of Attacker Armies")
plt.ylabel("Attacker Win Probability")
plt.title("Probability of Attacker Winning the Territory")
plt.grid(True)
plt.show()
