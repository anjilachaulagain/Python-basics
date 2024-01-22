try:
    f = open("hello.txt", "w")
    f.write("ram")
    text = f.readlines()
    print(text[-1])
    f.close()
except Exception as e:
    print(e)