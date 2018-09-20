# age = input ('please enter your age:')

# if int(age) >= 18:
#     print('adult')
# elif int(age) >= 6:
#     print('teenager')
# else:
#     print('kid')

# #nested conditionals

# if x==y:
#     print ('x and y are equal')
# else: if x<y :
#         print

# weight = input ('please enter your weight:')
# height = input ('please enter your height:')

# def calculate_bmi(weight,height):
#     bmi = weight/height
#     print('Your bmi is {:.1f}.'.format(bmi))
#     if bmi <= 18.5:
#         print ('underweight')
#     elif 18.5 <= bmi <= 25:
#         print ('normal weight')
#     elif 25 <= bmi <= 30 :
#         print('overweight')
#     else:
#         print('obesity')

# calculate_bmi()

# def compare (varA, varB):
#     if isinstance (varA,str) or isinstance (varB,str):
#         print('string involved')
#     else:
#         if varA > varB :
#             print('bigger')
#         elif varA == varB:
#             print('equal')
#         else:
#             print('smaller')

# a = 'hello'
# b = 3
# c = 5

# compare (a,b)
# compare (b,c)

# def diff21(n):
#     """
#     Given an int n, return te absolute difference between n and 21, except return double the absolute difference if n is over 21.
#     """
#     if n>21 :
#         return abs(n-21)*2
#     else:
#         return abs(n-21)
    
# print (diff21(19))

# def cigar_party(cigars, is_weekend)

# '''
# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
# '''
# if is_weekend and cigars >= 40  or 40 <= cigars <=60

# print(cigar_party(30,False))

def countdown (n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown (n-1)

# countdown(5)

def print_n (s,n):
    if n <= 0:
        return
    print (s)
    print_n (s,n-1)