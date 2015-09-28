__author__ = 'bipolar_coon_two'

import math

figure = input('Your figure is = ')

if figure == 'circle':
    x = input('radius = ')

elif figure == 'square':
    x = input('side = ')

else:
    print("Sorry, but I don't know this figure")
    exit(1)

try:
    x = int(x)

except:
    print('Sorry, but you entered is not a number')
    exit(1)

if x > 0 and figure == 'circle':
    S = math.pi * x * x
    print('Area of your circle is %.2f' % S)

elif x > 0:
    S = x * x
    print('Area of your square is %.2f' % S)

else:
    print('Sorry, I think is not a ' + figure)
