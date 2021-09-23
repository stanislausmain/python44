from abc import abstractclassmethod
from typing import Match

import math
x = int(input("Enter the number of seconds: "))
h = math.floor(x // 3600)
m = math.floor((x - h*3600) // 60)
s = x - h*3600 - m*60
assert x <= 86400, 'Invalid number of seconds'
print(str(h) + ' ' + str(m) + ' ' + str(s))

