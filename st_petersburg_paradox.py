import random
import matplotlib.pyplot as plt

def st_petersburg_game():
    flips = 0
    winnings = 0
    while True:
        flips += 1
        #Tails = 0, Heads = 1
        if random.randint(0, 1) == 0:  # Tails
            winnings = 2 ** flips
            return flips, winnings

def simulate_games(num_games):
    total_winnings = 0
    max_winnings = 0

    for x in range(num_games):
        flips, winnings = st_petersburg_game()
        total_winnings += winnings
        max_winnings = max(max_winnings, winnings)

    avg_winnings = total_winnings / num_games
    return avg_winnings, max_winnings

# Simulate the game 100, 10k, 1 million, and 10 million times
avg_winnings_100, max_winnings_100 = simulate_games(100)
print("Simulating 100 games:")
print(f"Average amount of money won per game: ${avg_winnings_100}")
print(f"Most money ever won in a game: ${max_winnings_100}\n")
avg_winnings_10k, max_winnings_10k = simulate_games(10000)
print("Simulating 10,000 games:")
print(f"Average amount of money won per game: ${avg_winnings_10k}")
print(f"Most money ever won in a game: ${max_winnings_10k}\n")
avg_winnings_mil, max_winnings_mil = simulate_games(1000000)
print("Simulating 1,000,000 games:")
print(f"Average amount of money won per game: ${avg_winnings_mil}")
print(f"Most money ever won in a game: ${max_winnings_mil}")
avg_winnings_10mil, max_winnings_10mil = simulate_games(10000000)
print("Simulating 10,000,000 games:")
print(f"Average amount of money won per game: ${avg_winnings_10mil}")
print(f"Most money ever won in a game: ${max_winnings_10mil}")

