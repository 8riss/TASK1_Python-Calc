
def calc():
    try:
        x = float(input("Value 1: "))
        z = input("Operator: ")
        y = float(input("Value 2: "))
        if (z == "+"):
            q = x+y
            print (q)
        else: print(" ")
        
        if (z == "-" ):
            q = x-y
            print (q)
        if (z == "/"):
            q = x/y
            print (q)
        if (z == "*"):
            q = x*y
            print(q)
        

    except: print("ERROR!")


print (calc())
