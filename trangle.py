a=float(input("a"))
b=float(input("b"))
c=float(input("c"))


def typetrangle():
    if a>0 and b>0 and c>0 :
        if (a<90 and b<90 and c<90) and (a+b+c==180):
            print("acute")
        elif (a==90 or b==90 or c==90) and (a+b+c==180):
            print("right")
        elif (a>90 or b>90 or c>90) and (a+b+c==180):
            print("obtuse")
        else:
            print("invalid input")
    else:
        print("invalid input")

typetrangle()
