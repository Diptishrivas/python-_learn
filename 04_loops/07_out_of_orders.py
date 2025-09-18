flavours = ["Ginger", "out of stock","Lemon", "Discontinued", "tulsi"]


for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "Discontinued":
      break
    print(f"{flavour} item found")
    
print(f"Out side of loop")
