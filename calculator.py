print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
    print(num1, " + ", num2, " = ", result)
elif choice == '2':
    result = num1 - num2
    print(num1, " - ", num2, " = ", result)
elif choice == '3':
    result = num1 * num2
    print(num1, " X ", num2, " = ", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(num1, " / ", num2, " = ", result)
    else:
        print("Division by zero is not possible")
else:
    print("Invalid input")

