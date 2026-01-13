class ChaiOrder:
    def __init__(self, type_, size):
          self.type =type_
          self.size =size
    
    def summary(self):
         return f"{self.size}ml of {self.type} chai."

order= ChaiOrder("Ginger",220)

print(order.summary())

order_two= ChaiOrder("Masala", 220)
print(order_two.summary())


# ////////////////////////////////////////////////////////////////////////////////////////////////////

class Hyundai:
    def __init__(self, model, color):
           self.model= model
           self.color=color
    def details(self):
         return f"I wanna BUY Hyndai {self.model} in {self.color} color that i saw in the showroom just love it in one view "

car = Hyundai("Creata", "black")
car_two=Hyundai("i20","white")
print(car.details())
print(car_two.details())