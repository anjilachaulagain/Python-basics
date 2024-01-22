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
print ("My name is {}". format(Person['name']))
print (f"My name is {(Person['name'])}. My age is {(Person['age'])}")
print (f"My hobby is {(Person['hobby'])}. My percentage is {(Person['Percentage'])}")
print (f"My family members are {(Person['Family_member'])}")
print(Person['Family_member'][1][2])