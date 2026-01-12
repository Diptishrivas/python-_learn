class Chai:
    origin='India'

print(Chai.origin)

Chai_is_hot=True
print(Chai_is_hot)


#creating object from chai


masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")
masala.is_hot= False

print(f"Class:{Chai.is_hot}")
print(f"Masala{masala.is_hot}")