
# This program will just ask how many objects are unclassified at 
# the time and will put them into an array based on other prereq 


import random

unid = input("Enter the amount of unclassified objects ")

objects = []

x = 0


# a series of prereq will go here such as color, time, slopes etc.
# after all those requirements are met it will classifiy it into a 1 of 2
# this code here just puts 1 into a transient and 2 into a nontransient
# into an array

while x < unid:
	
	prereq = random.randint(1,2) 

	

	if prereq == 1:

		# for i in xrange(unid):
		objects.insert(x, "Transient")

			
		x += 1
		print "Based on the slope, this obejct is Transient\n"
		print "-----------"	

	elif prereq == 2:

		# for i in xrange(unid):
		objects.insert(x, "Nontransient")
			

		x += 1
		print "Based on the slope, this obejct is Nontransient\n"
		print "-----------"	


print "The array:\n"
from pprint import pprint
pprint(objects)
	
