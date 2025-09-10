chai_order = dict (type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")


chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe base: {chai_recipe['base']}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar'in chai_order }")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# print(f"order details (keys): {chai_order.keys()}")
# print(f"order details (keys): {chai_order.values()}")
# print(f"order details (keys): {chai_order.items()}")

last_items = chai_order.popitems()
print(f"Removed last items: {last_items}")

extra_spices ={"cardamon": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("note", "No Note")
print(f"customer_note is: {customer_note}") 





