#a---------------------
import os

os.mkdir('new_directory')
os.rename('old_file.txt', 'new_file.txt')

print(os.getcwd())

#b----------------------

import sys

print(sys.argv)
print(sys.version)

#c----------------------
import math

print(math.sqrt(25))
print(math.cos(math.pi/4))

#d------------------------
import datetime

now = datetime.datetime.now()
print(now)

date = datetime.date(2022, 2, 14)
print(date)

time = datetime.time(12, 30, 0)
print(time)

#e------------------------
import random

print(random.randint(1, 10))

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
