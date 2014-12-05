"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution = 3(Largest Prime factor of 600851475143)

"""
import time
startTime = time.clock()

def prime(num):
	if num < 2: return False
	if num % 2 == 0: return num == 2

	division = 3

	while (division * division) <= num:
		if num % division == 0:
			return False
		division += 2
	
	return True
def max(list):
	for i in range(len(list)):
		max = list[i]
		if list[i] > max:
			list[i] = max
	return max

limit = 2000
number = 600851475143
output = []
i = 0
while i <= number:
	if prime(i) is True:
		if number % i == 0:
			output.append(i)
			print "Prime num found->> {}".format(i)
	i += 1
print max(output)
print "Program took %.4f secs to execute\n"%(time.clock() - startTime)



