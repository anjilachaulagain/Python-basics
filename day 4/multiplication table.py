# a = int(input("Enter the number: "))
# for index,b in enumerate(range(1,11)):
#     print(a,"*", index+1,"=",a*b)
    
    

Person = {
    'name':'Anjila',
    'age': 23,
    'Percentage': 99,
    'Family_member':(
        'mom',
        'dad',
        'sister'
    ),
    'hobby':(
        'reading',
        'watching movie',
    )
    }
for index,person in enumerate(Person):
    
    print(index+1,person,Person[person])


# while True:
#     a = int(input("Enter the first number:"))
#     b = int(input("Enter the second number: " ) )
#     operator= input("Enter the operator: ")
#     if operator == "+" :
#         result = a + b
#     elif operator == " - " :
#         result = a - b
#     elif operator == "*":
#         result = a * b
#     elif operator == "/":
#         result = a / b
#     elif operator == "f/":
#         result = a // b
#     elif operator == "^":
#         result = a**b
#     elif operator == "%":
#         result = a % b
#     else:
#         result = "Invalid operator."
        
#     print(f"{a} {operator} {b} = {result}")

