#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 1(Sum of all numbers divisible by 3 and 5 in range(1000))

sum = 0

for i in range(1000):
	if i % 5 == 0 or i % 3 == 0:
		sum += i

print sum