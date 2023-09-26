import random
import matplotlib.pyplot as plt


#Assume that both the attacker and defender have 10 armies at the beginning of the battle, and assume that the attacker continues the battle
# until the territory is won or the attacker only has a single army remaining. Your task is to estimate the probability for each possible number
# of remaining armies of each player at the end of this battle. The possibilities are the attacker could have any number two through ten, and
# the defender zero, or the attacker could have only one army remaining
# and the defender could have any number, one through ten. Display these
# probabilities nicely either in a table or a plot.
def ten_versus_ten_simualtion():
    a_starter_armies = 10
    d_starter_armies = 10

    results = {'A10D0': 0, 'A9D0': 0, 'A8D0': 0, 'A7D0': 0, 'A6D0': 0, 'A5D0': 0, 'A4D0': 0, "A3D0": 0, "A2D0": 0,
               'A1D1': 0, 'A1D2': 0, 'A1D3': 0, 'A1D4': 0, 'A1D5': 0, 'A1D6': 0, 'A1D7': 0, 'A1D8': 0, 'A1D9': 0, 'A1D10': 0 }

    num_simualtions = 10000

    for x in range(num_simualtions):
        a_battle_armies = a_starter_armies
        d_battle_armies = d_starter_armies


        while (d_battle_armies > 0 and a_battle_armies > 1):
            a_dice = min(a_battle_armies - 1, 3)
            d_dice = min(d_battle_armies, 2)
            
            a_rolls = sorted([random.randint(1, 6) for y in range(a_dice)], reverse=True)
            d_rolls = sorted([random.randint(1, 6) for y in range(d_dice)], reverse=True)


            for z in range(min(a_dice, d_dice)):
                if a_rolls[z] > d_rolls[z]:
                    a_battle_armies -= 1
                else:
                    d_battle_armies -= 1

        #Check results and add the result to the proper key
        #Theres probably a much cleaner way to do this but I can't be bothered rn
        #Also screw python for not havign switch statements
        if (a_battle_armies > 1 and d_battle_armies == 0):
            if (a_battle_armies == 2):
                results['A2D0'] = results['A2D0'] + 1
            elif (a_battle_armies == 3):
                results['A3D0'] = results['A3D0'] + 1
            elif (a_battle_armies == 4):
                results['A4D0'] = results['A4D0'] + 1
            elif (a_battle_armies == 5):
                results['A5D0'] = results['A5D0'] + 1
            elif (a_battle_armies == 6):
                results['A6D0'] = results['A6D0'] + 1
            elif (a_battle_armies == 7):
                results['A7D0'] = results['A7D0'] + 1
            elif (a_battle_armies == 8):
                results['A8D0'] = results['A8D0'] + 1
            elif (a_battle_armies == 9):
                results['A9D0'] = results['A9D0'] + 1
            elif (a_battle_armies == 10):
                results['A10D0'] = results['A10D0'] + 1
        elif (d_battle_armies > 0 and a_battle_armies == 1):
            if (d_battle_armies == 1):
                results['A1D1'] = results['A1D1'] + 1
            elif(d_battle_armies == 2):
                results['A1D2'] = results['A1D2'] + 1
            elif(d_battle_armies == 3):
                results['A1D3'] = results['A1D3'] + 1
            elif(d_battle_armies == 4):
                results['A1D4'] = results['A1D4'] + 1
            elif(d_battle_armies == 5):
                results['A1D5'] = results['A1D5'] + 1
            elif(d_battle_armies == 6):
                results['A1D6'] = results['A1D6'] + 1
            elif(d_battle_armies == 7):
                results['A1D7'] = results['A1D7'] + 1
            elif(d_battle_armies == 8):
                results['A1D8'] = results['A1D8'] + 1
            elif(d_battle_armies == 9):
                results['A1D9'] = results['A1D9'] + 1
            elif(d_battle_armies == 10):
                results['A1D10'] = results['A1D10'] + 1


    return results

results =  ten_versus_ten_simualtion()

#convert all values in the dictonary to percentages
for key in results:
   results[key] = ((results[key]/10000.0) * 100) 


# Extract keys and values from the dictionary
categories = list(results.keys())
values = list(results.values())

# Create a bar chart
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(categories, values)

# Label the axes and add a title
plt.xlabel('Final Number of Dice')
plt.ylabel('Percentage of Time Result Occurs')
plt.title('Simulated Outcomes for 10v10 RISK Battle')

# Display the chart
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Ensure all labels and titles are visible
plt.show()

