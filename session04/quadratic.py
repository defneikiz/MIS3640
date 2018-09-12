#Quadratic Excercise
def quadratic():
    from math import sqrt
    print ("This program will allow you to solve for quadratic equations \"ax^2 + bx + c = 0\".")
    a= int(input("Please enter the value for a:"))
    b= int(input("Please enter the value for b:"))
    c= int(input("Please enter the value for c:"))
    print()
    discriminant= (b**2)-(4*a*c)
    if discriminant<0 :
        print ("No real solutions")
    else:
        discriminant1= (sqrt(discriminant))
        root= (-b+ discriminant1) / (2*a), (-b-discriminant1) / (2*a)
        print("The root(s) of this quadratic equation is: {0}".format(root))

quadratic()
