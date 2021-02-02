#!/usr/bin/env python

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))
  
my_list = [len(name) for name in list_of_names]
print(my_list)

from person import *

people = {}

for n in range(len(list_of_names)):
  people[list_of_names[n]] = Person(
    name = list_of_names[n],
    age = list_of_ages[n],
    height = list_of_heights_cm[n])

import numpy
age_array = numpy.array(list_of_ages)
height_array = numpy.array(list_of_heights_cm)

average_age = numpy.mean(age_array)
print (" The Average age is:", average_age)

import matplotlib.pyplot as plt
x = [23,24,19,86]
y = [175,162,178,182]
#plt.plot([23, 24, 19, 86], [175, 162, 178, 182])
plt.xlabel('Age')
plt.ylabel('Height')
plt.title("Age vs Height")
plt.scatter(x, y)
plt.grid()
plt.savefig('Hw1scatterplot.png')
plt.show()
