#!/usr/bin/env python3

import sys

number = int(sys.argv[1])

print (number)
if number > 0:
	print ("Positive")
	if number < 50:
		if number%2 == 0:
			print ("It is an even number that is smaller than 50")
	elif number > 50 and number%3==0:
		print ("It is larger than 50 and divisible by 3")
elif number < 0 :
	print ("Negative")
elif number == 0:
	print ("Zero")

