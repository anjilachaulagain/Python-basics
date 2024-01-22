while True:
    try:
        a = int(input("number:"))
        b= int(input("number:"))
        if a==5:
            raise Exception("first number cannot be 5")
    
        print(a/b)
    except ZeroDivisionError:
        print("Zero cannot be divided")
        
    except ValueError:
        print("Please enter number only")
    except Exception as e:
        print("simething went wrong", e)
    except:
        print('something went wrong')
