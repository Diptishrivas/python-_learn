#String -indexing,slice and Encoding

chai_type ="Ginger chai"
customer_name = "priya"

print(f"Order for {customer_name} : { chai_type} please ! ")

chai_description = "Aromatic and  Bold more"
print(f"First word : {chai_description[0:8:2]}")
print(f"last word : {chai_description[12:]}")
print(f"last word : {chai_description[::-1]}")

lable_text = "chai Special "
ecoded_lable = lable_text.encode("utf-8")
print(f"Non Encoded lable: {lable_text}")
print(f"Encoded lable: {ecoded_lable}")
decoded_lable = ecoded_lable.decode("utf-8")
print(f"Decoded label : {decoded_lable}")