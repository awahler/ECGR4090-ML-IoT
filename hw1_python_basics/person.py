#!/usr/bin/env python


#list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
#list_of_ages  = [23, 24, 19, 86]
#list_of_heights_cm = [175, 162, 178, 182]

class Person():
	def __init__(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height
	def years_old(self):
     		print(self.name, 'is', self.age, 'years old ')

p = Person('Roger', 23, 175)

p.years_old()

def __repr__(self):
	return f'Car(self.name is self.age and self.height cm tall)'
