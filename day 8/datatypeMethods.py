# name ="""HELLO WORLD"""
# print(len(name))
# print(name.lower())
# print(name.upper())
# print(name.strip())
# print(name.split())

# fruits = [
#     'apple',
#     'apple',
#     'banana',
#     'orange',
# ]
# vegs=[
#     'sag',
#     'tomato',
#     'carrot'
# ]

# print(fruits)
# fruits.append("kiwi")
# print(fruits)

# fruits.extend(['mango','chocolate'])
# fruits.extend(vegs)
# print(fruits)
# fruits.insert(0,'sweetpotato')
# print(fruits)

# fruits.remove('orange')
# print(fruits)

# fruits.pop(0)
# print(fruits)

# fruits.index('apple')
# print( fruits)

# fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)



Person = {
    'name':'Anjila',
    'age': 23,
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
print(len(Person))

Person.keys()
print(Person)

Person.values()
print(Person)

Person.items()
print(Person)

Person.get('age',23)
print(Person)

Person.pop('age')
print(Person)

Person.update({"address":"Naryatar"})
print(Person)






