print("1.add(+)")
print("2.sub(-)")
print("3.mul(*)")
print("4.div(/)")

choice = input("Enter the choice num(1-4): ")

num1 =int(input("Enter the num1:"))
num2 =int(input("Enter the num2:"))

if choice == '1':
    result =num1+num2
    print("Ans:",result)

elif choice == '2':
    result= num1 - num2
    print("Ans:", result)

elif choice == '3':
    result =num1 * num2
    print("Ans:", result)

elif choice == '4':
    if num2 !=0:
        result = num2 / num1
        print("Ans:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid choice!")


