#basics of list
ingredients = ["water", "milk", "black", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
 
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

last_added =chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")

chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")

sugar_levels= [8,6,7,0,4,5,1]
print(f"Minimum sugar level : {min(sugar_levels)}")




