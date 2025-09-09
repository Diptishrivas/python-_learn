#tuples -( ) ,[ ] ,{ } and menbership testing
masala_spices = ( "cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardramom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C:{cardramom_ratio}")
ginger_ratio, cardramom_ratio =cardramom_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cardramom_ratio}")


#membership

print(f"Is ginger in masala spices ? {'ginger' in masala_spices} ")
print(f"Is ginger in masala spices ? {'cinnamon' in masala_spices} ")
print(f"Is ginger in masala spices ? {'Cinnamon' in masala_spices} ")



