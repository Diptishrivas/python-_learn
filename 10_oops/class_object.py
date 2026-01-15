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



# Percentage Calculator

total_marks = float(input("Enter total marks: "))
obtained_marks = float(input("Enter obtained marks: "))

percentage = (obtained_marks / total_marks) * 100

print("Your Percentage is:", round(percentage, 2), "%")
