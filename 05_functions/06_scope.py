def chai_counter():
    chai_order = "lemon"  # enclosing scope

    def print_order():
        chai_order = "Ginger" 
        print("Inner:", chai_order)

    print_order()
    print("Outer", chai_order)

chai_order = "Tulsi"
chai_counter()
print("Global :", chai_order)
