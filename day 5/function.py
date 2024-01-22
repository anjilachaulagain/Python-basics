# Positional argument

# def hello (first_person, second_person):
#     print(f'hello,{first_person}')
#     print(f'hello,{ second_person}')
    
# hello("ram", "shyam")
# hello("binit", "binita")

# keyword argument

# def person(f_name, m_name, l_name ):
#     print(f"hello {f_name} {m_name} {l_name}")
    
# person(m_name="Prasad" , f_name="Govinda", l_name="Chaulagain")


# def person(f_name, m_name, l_name , num=1):
#     print(f"hello {f_name} {m_name} {l_name}\n"*num)
    
# person(m_name="Prasad" , f_name="Govinda", l_name="Chaulagain", num=3)

# args
# def person(*args):
#     print(args[0], args[1], args[-1])
    
# person('name','age', 86, 727, 763555,'test')


# sum function
# args numbers
# print sum of all the number passed from args
# def sum(*numbers):
#     total = 0
#     for number in numbers:
#         total= total + number
#     print(total)
        
# sum(1,3,4,2,1,1,2)



def detail(f_name, m_name,l_name, faculty, college, interest1, interest2, p_address, t_address, affiliate):
    print(f"""I am {f_name} {m_name} {l_name}, a {faculty} student at {college} Affilated by {affiliate}. I have a keen interest in {interest1}{interest2}, and I aspire to pursue a career in the IT sector. I am originally from {p_address}, but I currently reside in {t_address}. """)

detail(f_name="Anjila", m_name="", l_name="Chaulagain", faculty="Bachelor in Computer Science (BCA)", college="Lumbini Academy College", affiliate="Tribhuvan University", interest1="WebDeveloper", interest2="", p_address="Jhapa", t_address="Naryantar")

