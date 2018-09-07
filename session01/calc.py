#question 1
import math
print('The volume of a sphere with a radius of 5 is: {}'.format ((4/3)* math.pi*(5**3)))
#question 2
cover = 24.95
bscover = cover * 0.6
bscover = round(bscover,2)
shipping = 3
shippingx = 0.75
order = 60
total_price = (bscover * order) + (shipping) + ((order-1)*shippingx)
print ('The total wholesale cost for 60 copies is : ${0}'. format(total_price))
original = 82
new = 89
percent_increase = round ((new - original) / original, 3)
percent_increase = percent_increase * 100
print ('The percent increase is {0}%.'.format(percent_increase))
