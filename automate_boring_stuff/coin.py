import random
'''Print the percentage of 10,000 experiments of 100 coin flips that contain a streak of 6 heads or 6 tails.'''
EXPERIMENTS = 10_000
num_streaks = 0

for experiment in range(EXPERIMENTS):
    results = []
    for _ in range(100):
        results.append(random.choice(["H", "T"]))
    
    for i in range(len(results)- 5):
        if results[i:i+6] == ["H"] * 6 or results[i:i+6] == ["T"] * 6:
            num_streaks += 1
            break
print(f"Chance of streak: {(num_streaks / 100)}")