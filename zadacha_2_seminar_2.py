b = int(input("Введите сумму: "))
c = int(input("Введите произведение: "))
from math import *

a = 1
x = round((b - sqrt((b**2) - 4 * a * c)) / 2 * a)
y = round((b + sqrt((b**2) - 4 * a * c)) / 2 * a)
print(x,y)