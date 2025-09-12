# size = input("choose your cup size(small/medium/larger)").lower()

# price = {
#     "small":10,
#     "medium":15,
#     "large":20
# }
 
# if size in price:
#     print(f"price of cup is {price[size]} ")

# else:
#     print("Sorry ! Unknown cup size")

cup = input("Enter the cup size(s/m/l)").lower()

if cup == "small":
    print(f"price is 10")
elif cup == "medium":
    print(f"price is 15")
elif cup == "large":
    print("price is 20")
else:
    print("Unavailable")
