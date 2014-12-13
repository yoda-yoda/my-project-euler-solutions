#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 160(Factorial trailing digits (last 5 excluding zeros))
License type: MIT :)
Status: PENDING...
"""
import time
startTime = time.clock()

def iterative_fact(num):
	product = 1
	for i in xrange(num):
		product *= i + 1
	return product

a = str(iterative_fact(1000)).replace("0","").replace("", "-").split("-")
print"\n\t {}".format(a[-6:])
time_diff = time.clock() - startTime
print "\tRun time... %.5f(secs) or %.5f(mins)" % (time_diff, (time_diff / 60.0))