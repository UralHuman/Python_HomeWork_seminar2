n = int(input("Введите число: "))
stepen = 0
count = 0
from math import *

while n >= stepen + 2:
    stepen = round(pow(2, count))
    count += 1
    if stepen <= n:
        print(stepen, end=" ")
