# coding: utf-8

# 8.4.2016 using module time

import time

def calcProd():
	product = 1
	for i in range(1, 500000):
		product *= i
	return product
	
startTime = time.time()
prod = calcProd()
endTime = time.time()

print('result length = %s  ' % (len(str(prod))) )
print('time %s' % (endTime - startTime))
