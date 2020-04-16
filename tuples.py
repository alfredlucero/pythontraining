# python tuples.py
# Tuple
# Immutable list (use when data should not change), ordered
# Values accessed by index
# Iteration, looping, concatenation
fruits_tuple = ("apple", "strawberry", "orange")
print(type(fruits_tuple))

for fruit in fruits_tuple:
    print(fruit)

(apple, strawberry, orange) = fruits_tuple
print(apple)
print(strawberry)
print(orange)

fruits_list = list(fruits_tuple)
print(type(fruits_list))

# tuple()


def high_and_low(numbers):
    highest = max(numbers)
    lowest = min(numbers)
    return (highest, lowest)


lottery_numbers = [16, 7, 10, 5, 4]
(highest, lowest) = high_and_low(lottery_numbers)
print(highest)
print(lowest)

sports_teams_championships = [("Lakers", 15), ("Celtics", 16)]
for (team, num_championships) in sports_teams_championships:
    print("Team {} won {} championships".format(team, num_championships))

# del tuple_name
