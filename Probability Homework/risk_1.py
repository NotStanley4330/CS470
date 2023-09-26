import random


#  If the attacker rolls na dice and the defender nd, what are the probabilities
# of the different outcomes (number of armies lost by each player)? Repeat
# for the different possible combinations of na (1,2,3) and nd (1,2). Is it ever
# advantageous for a player to roll less than the most dice they are allowed
# by the rules?


def simulate_battle(na, nd, num_samples=100000):
    attacker_wins = 0
    defender_wins = 0
    tie = 0
    
    for _ in range(num_samples):
        attacker_dice = sorted([random.randint(1, 6) for _ in range(na)], reverse=True)
        defender_dice = sorted([random.randint(1, 6) for _ in range(nd)], reverse=True)
        
        for a, d in zip(attacker_dice, defender_dice):
            if a > d:
                defender_wins += 1
            elif a < d:
                attacker_wins += 1
            else:
                tie += 1
    
    total = attacker_wins + defender_wins + tie
    return attacker_wins / total, defender_wins / total, tie / total

# Simulate and print results for all combinations of na and nd
results = {}
for na in range(1, 4):
    for nd in range(1, 3):
        attacker_win_prob, defender_win_prob, tie_prob = simulate_battle(na, nd)
        results[(na, nd)] = (attacker_win_prob, defender_win_prob, tie_prob)
        print(f"na={na}, nd={nd}: Attacker Wins: {attacker_win_prob:.4f}, Defender Wins: {defender_win_prob:.4f}, Tie: {tie_prob:.4f}")
