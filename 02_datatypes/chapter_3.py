#interger

black_tea_grams =14
ginger_grams = 3


total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")


remaining_tea =black_tea_grams - ginger_grams
print(f"Total grams of remaing tea is {remaining_tea}")


milk_liters = 7
serving = 4
milk_per_serving = milk_liters / serving
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")

total_cardom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardom_pods % pods_per_cup
print(f"Left over pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_falvour =base_flavor_strength ** scale_factor
print(F"scaled flavour strength {powerful_falvour}")
#2*2*2

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves : {total_tea_leaves_harvested}")