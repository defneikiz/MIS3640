
def gcd(a,b):
    '''
    Calculates greatest common divisor for a and b.
    '''
    if b==0:
        return a
    else:
        return gcd (b, a%b)

print('The greatest common divisor is {}.'.format(gcd(20,8)))