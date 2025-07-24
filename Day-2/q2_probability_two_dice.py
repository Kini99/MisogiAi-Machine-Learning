import random

count_sum_7 = 0
count_sum_2 = 0
count_sum_greater_10 = 0

for i in range(10000):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    dice_sum = die1 + die2
    if dice_sum == 7:
        count_sum_7 += 1
    if dice_sum == 2:
        count_sum_2 += 1
    if dice_sum > 10:
        count_sum_greater_10 += 1

prob_sum_7 = count_sum_7 / 10000
prob_sum_2 = count_sum_2 / 10000
prob_sum_greater_10 = count_sum_greater_10 / 10000

# Print results
print(f"P(Sum = 7): {prob_sum_7:.2f}")
print(f"P(Sum = 2): {prob_sum_2:.2f}")
print(f"P(Sum > 10): {prob_sum_greater_10:.2f}")