# coding: utf-8
# 8.4.2016 using module time

import time

loops = 5
count = 10000

def calcProd():
	product = 1
	n = 1
	i = 1
	
	while n <= loops:
		print n,
	
		for i in range(1, count):
		  product *= i
		n += 1
		print i,
		
	return product
	
loopStartTime = time.time()
print('start')
prod = calcProd()
# print prod
loopEndTime = time.time()
print('end')

print(' ')
print('--------------')
print loops * count, 
print (' durchläufe')

print('result length = %s  ' % (len(str(prod))) )

resultTime = time.time()

print('loop time %s' % (loopEndTime - loopStartTime))

print('convert time %s' % (resultTime - loopEndTime))

print('-----******------')
