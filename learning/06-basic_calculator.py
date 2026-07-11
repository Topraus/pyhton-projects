#basic calculator

operator = input("Choose an operator (+ , - , * , /): ")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if operator == "+":
    print(f"{num1} {operator} {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} {operator} {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} {operator} {num2} = {num1 * num2}")  
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f"{num1} {operator} {num2} = {num1 / num2}")
else:
    print("Please provide an operator.")