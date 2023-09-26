import random
import matplotlib.pyplot as plt

def monty_hall_simulation(num_games):
    switch_wins = 0
    stay_wins = 0
    switch_win_percentages = []
    stay_win_percentages = []
    total_games = 0

    for _ in range(num_games):
        # Randomly place the car behind one of the three doors
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)

        # Randomly pick a door to "guess"
        guess = random.randint(0, 2)

        # Find the door to reveal that has a goat and is not the guessed door
        reveal = None
        for i in range(3):
            if i != guess and doors[i] == 'goat':
                reveal = i
                break

        # Implement the switching strategy
        switch_guess = 3 - guess - reveal

        # Check if switching wins
        if doors[switch_guess] == 'car':
            switch_wins += 1

        # Check if staying wins
        if doors[guess] == 'car':
            stay_wins += 1

        total_games += 1
        switch_win_percentages.append(switch_wins / total_games * 100)
        stay_win_percentages.append(stay_wins / total_games * 100)

    return switch_win_percentages, stay_win_percentages

# Simulate at least 1000 games
num_games = 10000
switch_win_percentages, stay_win_percentages = monty_hall_simulation(num_games)

# Plot the results
plt.plot(range(1, num_games + 1), switch_win_percentages, label='Switch Strategy')
plt.plot(range(1, num_games + 1), stay_win_percentages, label='Stay Strategy')
plt.xlabel('Number of Games Played')
plt.ylabel('Win Percentage (%)')
plt.legend()
plt.title('Monty Hall Simulation Results')
plt.show()

# Calculate the final percentages after all games
final_switch_percentage = switch_win_percentages[-1]
final_stay_percentage = stay_win_percentages[-1]

print(f"Percentage of wins with switching: {final_switch_percentage:.2f}%")
print(f"Percentage of wins with staying: {final_stay_percentage:.2f}%")
