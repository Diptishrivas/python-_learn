# value = 13
# remainder = value % 5

#if remainder:
 #   print(f"Not divisible ,remainder is {remainder}")

# if(remainder := value% 5):
#     print(f"Not Divisible , remainder is {remainder}")


#     available_sizes = ["small", "medium", "larger"]

#     if (requested_size := input ("Enter your chai cup size:")) in available_sizes:
#         print(f"Serving {requested_size}")
#     else:
#         print(f"Size is unavaible - {requested_size}")

flavours = ["masala", "ginger","lemon", "mint"]

print("Available flavors:", flavours)

while(flavour := input("choose your flavour:")) not in flavour:
    print(f"Sorry, {flavour} is  not available")
print(f"you choose { flavour} chai")
