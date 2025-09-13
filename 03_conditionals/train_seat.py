seat_type = input("Enter the seat type(s/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No Ac,beds available")
    case "ac":
        print("Ac- Air conditioned, comfy ride")
    case "general":
        print("General- cheapest option, no reservation")
    case "luxury":
        print("Luxury - premium seats with meals")
    case _:
        print("Unavailable seat")
    