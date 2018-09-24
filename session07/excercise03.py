from math import *
def mysqrt(a):
    '''
    Calculates square root.
    '''
    x=1
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.00000000001:
            break
        x = y
    return y

def test_square_root():
    '''
    Displays outcomes of calculating square root of a using different methods, and the absolute difference in between
    '''
    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"

    line2a="-"
    line2b="---------"
    line2c="-----------"
    line2d="----"

    spacing1=" "
    spacing2=" " * 3
    spacing3=""

    print(line1a,spacing1,line1b,spacing2,line1c,spacing3,line1d)
    print(line2a,spacing1,line2b,spacing2,line2c,spacing3,line2d)

    for i in range(9):
        i +=1
        a = i
        b = mysqrt(a)
        c = sqrt(a)
        d = abs(b-c)
        print('{:.1f} {:.10f}  {:.10f}  {}'.format(a, b, c, d))


test_square_root()
