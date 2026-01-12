class Chai:
    temp='hot'
    strength='strong'

cutting = Chai()

print(cutting.temp)
print(cutting.strength)

cutting.temp="Mild"
cutting.cup="small"

print(cutting.temp)
print(f"after change temp:{cutting.temp}")


del cutting.temp
del cutting.cup

print(f"{cutting.cup}")
print(f"{cutting.temp}")

#dekh bydefault yeh object m fallback krta h class k andr  or phir agr attribute m ni hua toh error de deta h



