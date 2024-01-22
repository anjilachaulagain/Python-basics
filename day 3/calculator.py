a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *,/, f/, ^, %): ")

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":       
    result = a / b
elif operator == "f/":       
    result = a // b
elif operator == "^":
    result = a**b
elif operator == "%":
    result = a % b
else:
    result = "Invalid operator."

print(f"{a} {operator} {b}= {result}")

